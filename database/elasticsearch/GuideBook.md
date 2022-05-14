# https://www.elastic.co/guide/en/elasticsearch/guide/master/_query_phase.html

# What is elasticsearch
Elasticsearch is an open-source search engine built on top of Apache Lucene™, a full-text search-engine library.

- A distributed real-time document store where every field is indexed and searchable
- A distributed search engine with real-time analytics
- Capable of scaling to hundreds of servers and petabytes of structured and unstructured data


# What to focus
## Manage
1.how to get your data in and out of Elasticsearch
2.how Elasticsearch interprets the data in your documents
3.how basic search works
4.how to manage indices

## Search
- deep dive into search

## Analyzer
- effective use of analyzers and queries

## Analytic
- aggregations and analytics

## Modeling
how to model your data to work most efficiently with Elasticsearch

## Monitor
important configurations, what to monitor, and how to diagnose and prevent problems.




# Getting Started :: Manage!!!
1.Life Inside a Cluster
2.Distributed Document Store
3.Distributed Search Execution,
4.Inside a Shard
- Proximity Matching and Partial Matching
- distributed processes at work


# Life Inside a Cluster
- terminology like cluster, node, and shard
- the mechanics of how Elasticsearch scales out
- how it deals with hardware failure.

- the processes at work inside Elasticsearch
- horizontal scale
- distributed by nature( other databases not )
- scale with your needs and to ensure that your data is safe from hardware failure.

Cluster
a cluster consists of one or more nodes with the same cluster.name that are working together to share their data and workload.

Node
A node is a running instance of Elasticsearch, 
As nodes are added to or removed from the cluster, the cluster reorganizes itself to spread the data evenly.
master node, which is in charge of managing cluster-wide changes like creating or deleting an index, or adding or removing a node from the cluster.
Every node knows where each document lives and can forward our request directly to the nodes???

+ 어떻게 모든 노드가 모든 문서를 찾아갈 수 있지?

Index
a place to store related data.
just a logical namespace that points to one or more physical shards.
our applications talk to an index not a shard directly.

Shard
- The number of primary shards is fixed at the moment an index is created. Effectively, that number defines the maximum amount of data that can be stored in the index.
- a low-level worker unit that holds just a slice of all the data in the index
- single instance of Lucene
- a fully fledged search engine in its own right, and is capable of using all of the resources of a single node
- a primary shard can technically contain up to Integer.MAX_VALUE - 128 documents
- Each document in your index belongs to a single primary shard, so the number of primary shards that you have determines the maximum amount of data that your index can hold.
- cluster grows or shrinks, Elasticsearch will automatically migrate shards between nodes so that the cluster remains balanced.

+ 인덱스 구성시 가장 먼저 고려해야 할 것? 도큐먼트의 사이즈 정하기. why? 한 번 프라이머리 샤드를 정하면 바꿀 수 없기 때문에.
+ 그렇다면 매일마다 생성되는 대량의 데이터는 어떻게 관리할 것인가?

# Replica Shard
A replica shard is just a copy of a primary shard.
Replicas are used to provide redundant copies of your data to protect against hardware failure,
and to serve read requests like searching or retrieving a document. => the more search throughput you can handle.
The number of replica shards can be changed dynamically on a live cluster, allowing us to scale up or down as demand requires.
triple search performance compared to our original three-node cluster.

+ 성능증가란 정확하게 어떤 것을 의미하는가? 속도인가? 검색 점수인가?

+ 레플리카가 많아지면 성능이 어떻게 영향을 미치지?
+ 레플리카 샤드와 프라이머리 샤드는 반드시  다른 노드에 위치해야 하는가?


Scale Horizontally
hardware resources (CPU, RAM, I/O) of each node are being shared among fewer shards, allowing each shard to perform better

- 노드 수가 증가하면 샤드에 사용하는 하드웨어 자원의 부하가 적어짐으로써, 샤드의 성능이 향상된다.
- 근데 다른 프로세스에 분산하는 기준이 무엇이지?


# 하드웨어 장애에 대처하는 방법
green : All primary and replica shards are active.
yellow : All primary shards are active, but not all replica shards are active.
red : Not all primary shards are active.

어떻게 샤드를 통합한다는 것이지? 과정을 자세하게 알 수 있나?

# 장애시에 내부적으로 일어나는 상황
the nodes elected a new master
would have seen status red: not all primary shards are active!
the new master node did was to promote the replicas of these shards on Node 2 and Node 3 to be primaries
This promotion process was instantaneous, like the flick of a switch.
So why is our cluster health yellow



# Distributed Document Store
how the data is distributed and fetched from the cluster

+ 이게 무슨 말이지?

shard = hash(routing) % number_of_primary_shards
- the number of primary shards can be set only when an index
- if the number of primary shards ever changed in the future, all previous routing values would be invalid and documents would never be found.
- the number of primary shards in the index to return the remainder.
- The remainder will always be in the range 0 to number_of_primary_shards - 1, and gives us the number of the shard where a particular document lives.
- A custom routing value could be used to ensure that all related documents—​for instance, all the documents belonging to the same user—​are stored on the same shard.


consistency
the primary shard requires a quorum, or majority, of shard copies (where a shard copy can be a primary or a replica shard) to be available before even attempting a write operation.

timeout
if insufficient shard copies are available, Elasticsearch waits, in the hope that more shards will appear.



the coordinating node will choose a different shard copy on every request in order to balance the load; it round-robins through all shard copies.
a replica might report that the document doesn’t exist


Why the Funny Format?

would create many more data structures that the Java Virtual Machine (JVM) would have to spend time garbage collecting.

# Shard question
- what is it?
- logical? physical?
- primary? replica?
- what relationship with indx?
- what is document in shard?



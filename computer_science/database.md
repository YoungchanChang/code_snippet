# DB 구조 & 설계

1. Primary key
  - 유일성, 최소성
  - cadidate key
  - 슈퍼키(유일성), 후보키(최소한의 속성), 대체키, 복합키(두 개 이상의 column으로 구성된 후보키)
  - alternative key, candidate key

2. 관계형 데이터베이스의 N:M 관계
  - 양쪽 entity 모두가 서로에게 1:N 관계
  - 보통 새로운 table(Mapping table)을 통해서 관계
  - 
2. left outer join, inner join 차이
 - inner join(또는 join)은 두 테이블에 모두 있는 내용만 join되는 방식
 - left outer join(또는 left join)은 왼쪽 table의 모든 행에 대해서 join을 진행

4. RDB - NoSQL를 비교
 - 관계형 데이터베이스(RDB)는 사전에 엄격하게 정의된 DB schema를 요구하는 `table` 기반 데이터 구조를 갖습니다.
 - NoSQL(비관계형 데이터베이스)은 table 형식이 아닌 `비정형 데이터`를 저장할 수 있도록 지원
 - 수평적 확장(scale out) 용이
 - 확장가능성 / 수정가능성
 - 데이터 update가 자주 이루어지지 않고 조회가 많은 경우, 또 scale out이 가능하므로 데이터 양이 매우 많은 경우
 - RDB는 데이터 구조가 명확하여 변경될 여지가 없는 경우, 또 데이터 중복이 없으므로 데이터 update가 잦은 시스템에서 사용

# Transaction
1. Transaction을 간단히 설명
- 데이터베이스 내에서 수행되는 작업의 최소 단위
- ACID(원자성, 일관성, 고립성, 지속성)의 4가지 규칙
- COMMIT과 ROLLBACK 명령어를 통해 데이터 무결성을 보장

2. DeadLock

# Index
1. Index의 필요성
- 테이블의 검색 성능을 높여주는 방법.
- B+Tree구조를 사용. 색인과 같은 역할을 한다.
- full table scan을 할 필요가 없다.

- Index => Btree, B+tree, Hash, Bitmap이 있다.
- 인덱스 생성시 데이터의 물리적 위치와 함께 별도 파일에 저장된다.
- 인덱스에 저장되는 속성 값이 search-key라고 한다. 물리적으로 저장한 위치를 pointer라고 한다.
- 특정 조건을 만족하는 데이터를 찾을 때 빠르게 찾을 수 있다.

- 클러스터형 인덱스 : 기본키로 지정
- 보조 인덱스 : 별도의 공간에 인덱스 생성. 인덱스 생성 혹은 고유키로 지정하면 된다.
- 

2. index를 어느 column
- 카디널리티(데이터가 중복되지 않는 정도)는 높고, 선택도(특정 값을 잘 골라낼 수 있는 정도)가 낮은 column을 선택해서 설정
- 데이터가 중복되지 않는 정도
- 선택도는 데이터에서 특정 값을 잘 골라낼 수 있는 정도를 뜻합니다.
- 선택도가 1이면 모든 데이터가 unique함을 의미합니다.

3. b+tree
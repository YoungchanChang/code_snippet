# 크론탭 설정

## certbot 갱신 설정

- 엔진엑스 종료 뒤, 인증서 갱신 후 엔진엑스 재시작

```commandline
0 0 1 * 8 /usr/bin/service nginx stop
0 1 1 * * /usr/bin/certbot certonly --force-renew -d <"mysite.co.kr"> <<< 2
0 2 1 * * /usr/bin/service nginx restart
```

- 참조 : https://crontab.guru/
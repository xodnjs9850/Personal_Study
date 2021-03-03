

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

shell_code() {
    setreuid(0, 0);     //reid, reid를 root로 설정
    setregid(0, 0);     //rgid, egid를 root 그룹으로 설정
    system("/bin/sh");  //root 및 root 그룹 권한으로 쉘 실행
}

int main(int argc, int **argv) {
    char buffer[12];                            //크기가 12바이트인 버퍼 생성
    memset(buffer, 0x00, sizeof(buffer));       //버퍼를 0으로 초기화
    if (argc != 2)
    {
        printf("Usage : buf_over data\n");
        exit(-1);
    }

    strcpy(buffer, argv[1]);                    // 인자로 받은 문자열을 버퍼로 복사
    printf("sizeof %d \n", sizeof(argv[1]));
    printf("strlen %d \n", strlen(argv[1]));
    return 0;
}
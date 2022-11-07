import java.util.Scanner;

public class operatorPractice {
    public static void main(String args[]) {
        // 증감연산자 (단항연산자)
        // ++, --
        // 전위연산과 후위연산 기능 제공

        // int bar = 2;

        // 전위연산
        // ++bar; // bar = bar + 1;
        // 전위연산은 증감연산위 처리된후 출력
        // System.out.println(++bar);

        // 후위연산
        // bar++; // bar = bar + 1;
        // 후위연산은 세미콜론을 만나고 난 후 연산처리
        // System.out.println(bar++);

        // int foo = bar++;
        // System.out.println(foo);
        // System.out.println(bar);

        // 키보드로부터 정수를 입력받아 아래 조건을 만족하면 '참' 출력.
        // 아니면 거짓
        // 입력값 참 조건 : 4 이상 10 미만

        // Scanner scn = new Scanner(System.in);

        // int inputValue = scn.nextInt();
        // if (inputValue >= 4 && inputValue < 10) {
        // System.out.println("참");
        // } else {
        // System.out.println("거짓");
        // }
        // scn.close();

        // && 는 앞의 조건이 False 면 뒤의 것은 실행 x
        // || 는 앞의 조건이 True 면 뒤의 것은 실행 x
        int bar = 2;
        if (3 < 4 || (bar = bar + 2) > 1)
            System.out.println("참");

        System.out.println(bar);
        // 이러한 조건문 사용은 좋지않음

    }
}

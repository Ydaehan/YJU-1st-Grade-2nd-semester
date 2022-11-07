import java.util.Scanner;

public class quiz1 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int selcetMenu = 0;
        int selectDan = 0;
        while (true) {
            // 메뉴 출력
            System.out.println("-------------------------");
            System.out.println("1. 구구단 출력");
            System.out.println("2. 프로그램 종료");
            System.out.println("-------------------------");
            selcetMenu = scn.nextInt();
            // 구구단 출력 /프로그램 종료 / 예외처리
            if (selcetMenu == 1) {
                System.out.println("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력");
                // 입력 범위 초과 예외 처리
                while (true) {
                    selectDan = scn.nextInt();
                    if (selectDan > 9 || selectDan < 2) {
                        System.out.println("2~9 사이의 정수를 입력해주세요");
                    } else {
                        break;
                    }
                }
                // 구구단 출력
                for (int num = 1; num < 10; num++) {
                    System.out.println(selectDan + " X " + num + " = " + selectDan * num);
                }
                // 프로그램 종료
            } else if (selcetMenu == 2) {
                System.out.println("이용해주셔서 감사합니다.");
                break;
            } else {
                System.out.println("잘못 입력하셨습니다. 다시입력하세요.");
            }
        }
        scn.close();
    }
}

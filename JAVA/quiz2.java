import java.util.Scanner;

public class quiz2 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int inputCount = 0;
        // 키보드로 부터 정수 값 입력
        while (true) {
            int inputValue = scn.nextInt();
            while (inputValue <= 0) {
                // 음수 입력시 "1이상 양수를 입력해주세요" 출력 후
                System.out.println("1이상 양수를 입력해주세요");
                // 재입력
                inputValue = scn.nextInt();
            }
            if (inputValue == 20000) {
                System.out.println("이용해주셔서 감사합니다.");
                break;
            }
            inputCount++;
            System.out.println(inputCount + "번째 입력 값은 = " + inputValue);
            if (inputValue % 2 == 0) {
                System.out.println("짝수 입니다.");
            } else {
                System.out.println("홀수 입니다.");
            }
            if (inputValue % 3 == 0) {
                System.out.println("3의 배수 입니다.");
            }
            if (inputValue % 7 == 0) {
                System.out.println("7의 배수 입니다.");
            }
        }
        scn.close();
    }
}

import java.util.Scanner;

public class plusQuiz2 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int inputCount = 0;
        String str;
        // 키보드로 부터 정수 값 입력
        while (true) {
            inputCount++;
            String result = inputCount + "번째 입력 값";
            str = scn.nextLine();
            // "q"를 입력 받아도 종료
            if (str.equals("q")) {
                System.out.println("이용해주셔서 감사합니다.");
                break;
            }
            int inputValue = Integer.parseInt(str);
            while (inputValue <= 0) {
                // 음수 입력시 "1이상 양수를 입력해주세요" 출력 후
                System.out.println("1이상 양수를 입력해주세요");
                // 재입력
                str = scn.nextLine();
                if (str.equals("q"))
                    break;
                inputValue = Integer.parseInt(str);
            }
            // 20000 입력시 종료
            if (inputValue == 20000 || str.equals("q")) {
                System.out.println("이용해주셔서 감사합니다.");
                break;
            }
            if (inputValue % 2 == 0)
                result += "\n짝수 입니다.";
            else
                result += "\n홀수 입니다.";
            if (inputValue % 3 == 0)
                result += "\n\t3의 배수 입니다.";
            if (inputValue % 7 == 0)
                result += "\n\t7의 배수 입니다.";
            System.out.println(result);
        }
        scn.close();
    }
}

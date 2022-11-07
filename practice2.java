import java.util.Scanner;

public class practice2 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String inputString = "";
        int inputValue = 0;
        int count = 0;
        // 키보드로 부터 정수 입력받기
        while (true) {
            try {
                // 예외 가능성이 있는 문장
                inputString = scn.next();

                inputValue = Integer.parseInt(inputString);
                while (inputValue <= 0) {
                    System.out.println("1이상의 양수 값을 입력하세요.");
                    inputValue = scn.nextInt();
                }
                if (inputValue == 20000) {
                    System.out.println("프로그램 종료");
                    break;
                }
                count++;
                String result = count + "번째 입력 값";
                // 짝수 또는 홀수
                if (inputValue % 2 == 0)
                    result += "\n짝수입니다.";
                else
                    result += "\n홀수입니다.";
                // 3의 배수
                if (inputValue % 3 == 0)
                    result += "\n\t3의 배수 입니다.";
                // 7의 배수
                if (inputValue % 7 == 0)
                    result += "\n\t7의 배수 입니다.";
                System.out.println(result);
            } catch (Exception e) {
                if (inputString.equals("q")) {
                    System.out.println("프로그램 종료");
                    break;
                }
            }
        }

        // 예외처리 1 'q' or '20000' 입력 시 종료
        // 예외처리 2 1 이상 정수 받기
        scn.close();
    }
}

import java.util.Scanner;

public class Practice1 {
    public static void main(String args[]) {
        // 키보드로 부터 정수를 입력 받아 아래 조건에 따라 결과 값 출력
        // 100 이하 90 이상 -> A
        // 90 미만 80 이상 -> B
        // 80 미만 70 이상 -> C
        // 70 미만 60 이상 -> D
        // 60 미만 -> F
        // 그 외 "잘못된 입력 값"

        Scanner scn = new Scanner(System.in);
        int inputValue = scn.nextInt();

        String result = "";
        // if (inputValue <= 100 && inputValue >= 90) {
        // System.out.println("A");
        // } else if (inputValue >= 80) {
        // System.out.println("B");
        // } else if (inputValue >= 70) {
        // System.out.println("C");
        // } else if (inputValue >= 60) {
        // System.out.println("D");
        // } else if (inputValue < 60 && inputValue >= 0) {
        // System.out.println("F");
        // } else {
        // System.out.println("잘못된 입력 값");
        // }

        if (inputValue > 100 || inputValue < 0) {
            result = "잘못된 입력 값";
        } else if (inputValue >= 90) {
            result = "A";
        } else if (inputValue >= 80) {
            result = "B";
        } else if (inputValue >= 70) {
            result = "C";
        } else if (inputValue >= 60) {
            result = "D";
        } else {
            result = "F";
        }
        System.out.println(result);
    }
}

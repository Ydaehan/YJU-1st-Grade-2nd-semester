import java.util.Scanner;
public class test1 {
    public static void main(String[] args) {
        // 키보드로부터 0~100 사이의 정수를 입력받아 A~F 등급을 출력하는 프로그램을 작성
        // 입력 값이 음수 또는 100 초과 경우 아래 error messager 를 출력하고 재입력 받기
        // "잘못된 입력 값 입니다. 다시 입력하세요."
        Scanner scn = new Scanner(System.in);
        System.out.println("점수를 입력 하세요");
        int inputValue = scn.nextInt();
        char grade;
        while(inputValue < 0 || inputValue > 100){
            System.out.println("잘못된 입력 값 입니다. 다시 입력 하세요");
            inputValue = scn.nextInt();
        }
        // A ~ F 100 을 초과하는지 검사를 또 할 필요가 없다.
        if(inputValue >= 90){
            grade = 'A';
        }else if (inputValue >= 80){
            grade = 'B';
        }else if (inputValue >= 70){
            grade = 'C';
        }else if (inputValue >= 60){
            grade = 'D';
        }else{
            grade = 'F';
        }
        System.out.println(inputValue + "의 등급은 " + grade + " 입니다");
        scn.close();
        }
    }
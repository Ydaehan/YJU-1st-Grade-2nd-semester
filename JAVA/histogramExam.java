import java.util.Scanner;
public class histogramExam {
    public static void main(String[] args) {
        // 키보드로부터 양의 정수 하나 N을 입력받고, N개의 정수형 배열 선언
        Scanner scn = new Scanner(System.in);
        System.out.println("배열의 개수를 입력하세요.");
        int inputValue = scn.nextInt();

        // 입력받은 N값이 1 이상 100이하의 값만 수용, 아닐 경우 Msg 출력 후 재입력
        while(inputValue > 100 || inputValue < 1){
            System.out.println("잘못 입력 하셨습니다. 1 ~ 100 사이 값을 입력하세요.");
            inputValue = scn.nextInt();
        }
        
        // 난수 배열의 초기값 설정
        int randArray[] = new int[inputValue];
        for(int reset = 0; reset < randArray.length; reset++){
            randArray[reset] = -51;
        }

        int randNum = 0;
        // 난수를 발생하여 배열에 저장
        for(int i = 0; i < inputValue; i++){
            randNum = (int)(Math.random() * 101 - 50);
            // 배열 내 중복값 제거
            for(int j = 0; j < randArray.length; j++){
                if(randNum == randArray[j]){
                    randNum = (int)(Math.random() * 101 - 50);
                    j = -1;
                }
            }
            randArray[i] = randNum;
            // 정렬 전 배열의 난수값
            // System.out.print(randArray[i] + " ");
        }

        // System.out.println(" ");
        int changingIndexNum = 0;
        // 최대값 최소값 구하기 전 정렬
        for(int k = 0 ; k < randArray.length; k++){
            for(int index = 0; index < randArray.length - 1; index++){
                changingIndexNum = randArray[index + 1];
                if(randArray[index] > randArray[index + 1]){
                    randArray[index + 1] = randArray[index];
                    randArray[index] = changingIndexNum;
                }
            }
        }


        // 출력
        System.out.println("배 열 의   개수 : " + inputValue);
        // 정렬 후 배열 내 난수 값
        System.out.print("배열 내 난수 값 : ");
        for(int check = 0 ;check < randArray.length; check++){
            System.out.print(randArray[check] + " ");
        }

        int max = randArray[inputValue - 1];
        System.out.println(" ");
        System.out.println("최\t댓\t값 : "+ max);
        // 최소값 구하기
        int min = randArray[0];
        System.out.println("최\t소\t값 : "+min);
        // 평균값 구하기, 실수 출력
        float avg = 0.0f;
        int sum = 0;
        for(int i = 0 ; i < randArray.length; i++){
            sum += randArray[i];
        }
        avg = ((float)sum / randArray.length);
        System.out.println("평\t균\t값 : "+avg);

        
        // 구간별 난수의 개수를 구하고 히스토그램으로 출력
        System.out.println("히스토그램");
        for(int h = -50; h <= 40; h+=10){
            // 구간 출력
            if(h == 40){
                System.out.print(h + " ~ " + (h + 10) + " : ");
            }else{
                System.out.print(h + " ~ " + (h + 9) + " : ");
            }
            
            // 구간 별 난수 개수 출력
            for(int checkValue = 0; checkValue < randArray.length; checkValue++){
                if(h < 40){
                    if(randArray[checkValue] >= h && randArray[checkValue] <= (h + 9)){
                        System.out.print("*");
                    }
                }else{
                    if(randArray[checkValue] >= h && randArray[checkValue] <= (h + 10)){
                        System.out.print("*");
                    }
                }
            
            }
            System.out.println("");
        }
        scn.close();
    }
}

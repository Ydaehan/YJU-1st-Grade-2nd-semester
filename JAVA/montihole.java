import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.List;
public class montihole {
    public static void main(String[] args) {
        // 3개의 문 중 2개는 inCorrect 1개는 correct
        // 첫번째 랜덤선택 후 inCorrect 인 문 하나를 개방
        // 그 후 선택을 바꾸고 결과 출력
        Random random = new Random();
        Scanner scn = new Scanner(System.in);
        // 시행횟수 입력
        System.out.println("시행횟수를 입력해주세요.");
        float playCount = scn.nextFloat();
        List<String> checkingCorrect = new ArrayList<String>();   // 당첨 카운트
        List<String> checkingInCorrect = new ArrayList<String>(); // 꽝 카운트
        int secondSelect = 0;
        for(int count = 1; count <= playCount; count++){
            boolean doorA = random.nextBoolean();
            boolean doorB = random.nextBoolean();
            boolean doorC = random.nextBoolean();
            // 시작 시 세 개 문은 랜덤한 true false 값을 가짐
            // 세 개의 문 중 하나에 true 값을 넣어 당첨 문을 선정하고 
            // 나머지 문은 false 값을 주어 꽝 설정
            if(doorA == true){
                doorB = false;
                doorC = false;
            }else if(doorB == true){
                doorA = false;
                doorC = false;
            }else if(doorC == true){
                doorA = false;
                doorB = false;
            }else{
                count --;
                continue;
            }
            int firstSelect = random.nextInt(2);
            boolean change = true; // 무조건 선택을 변경
            int changeSelect = random.nextInt(2);
            // 첫 선택 후 꽝 중에 하나의 문을 오픈
            int openDoorNum = random.nextInt(2);
            // 오픈할 문을 랜덤으로 선택하는데 오픈될 문과 처음 선택할 문이 겹치면 안됨
            while(openDoorNum == firstSelect){
                openDoorNum = random.nextInt(2);
            }
            // 처음 선택값이 바꿀 값과 같으면 안되며 ,마찬가지로 오픈할 문과도 같은 값이 되면 안됨
            while(openDoorNum == firstSelect || (firstSelect == changeSelect)){
                changeSelect = random.nextInt(2);
            }

            switch (firstSelect) {
                case 0:
                    if(change){
                        secondSelect = changeSelect;
                        // 선택을 바꿧을때
                        switch (secondSelect) {
                            case 0:
                                if(doorA == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                            case 1:
                                if(doorA == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                            case 2:
                                if(doorA == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                                break;
                        }
                    }
                case 1:
                    if(change){
                        secondSelect = changeSelect;
                        switch (secondSelect) {
                            case 0:
                                if(doorB == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                            case 1:
                                if(doorB == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                            case 2:
                                if(doorB == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                                break;
                        }}
                case 2:
                    if(change){
                        secondSelect = changeSelect;
                        switch (secondSelect) {
                            case 0:
                                if(doorA == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                            case 1:
                                if(doorA == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                            case 2:
                                if(doorA == true){
                                    checkingCorrect.add("당첨");
                                }else{
                                    checkingInCorrect.add("꽝");
                                }
                                break;
                    }
            }
        }
    }
    System.out.println(secondSelect);
        float percentage = checkingCorrect.size() / playCount;
        System.out.println("당첨 횟수 = " + checkingCorrect.size()); 
        System.out.println("꽝 횟수 = " + checkingInCorrect.size());
        System.out.println(percentage);
        scn.close();
}}

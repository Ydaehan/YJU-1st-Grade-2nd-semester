import java.util.Scanner;
public class TestArray {
    public static void main(String[] args) {
        // 야구게임만들기
        // 중복되지 않은 0~9 사이 정수를 3개 생성 math.random()
        // 순서상관 x
        // 키보드로 부터 정수 3개 입력 받아 strike, ball, out 판정
        // strike -> 값 일치 / ball -> 값 일치x but 3개중에 존재 / out -> ball 과 strike count = 0
        // 시도횟수 >= 5 or strike out == 2
        // 맞추면 win
        Scanner scn = new Scanner(System.in);
        
        final int RAND_NUM = 3;
        int computer_num[] = new int[RAND_NUM];
        int user_num[] = new int[RAND_NUM];

        // 0 ~ 9사이 중복되지 않은 난수를 발생하여, 배열에 저장
        int randNum = 0;
        for(int i = 0; i < RAND_NUM; i++){
            randNum = (int)(Math.random()*10);
            //중복 확인
            for(int j = 0; j < RAND_NUM; j++){
                if(randNum == computer_num[j]){
                    randNum = (int)(Math.random()*10);
                    j = -1;
                }
            }
            computer_num[i] = randNum;
            //System.out.println(computer_num[i]);
        }
        
        int inputNum = 0;
        int outC = 0;
        String result = "정답은 : ";
        int gameC = 1;

        while(true){
            System.out.println("시도횟수 : " + gameC);
            // 사용자로부터 0 ~ 9 사이 정수 입력(중복값 입력 안한다는 가정)
            System.out.println("정수 3개를 입력하세요");
            for(int k = 0; k < RAND_NUM; k++){
                inputNum = scn.nextInt();
                user_num[k] = inputNum;
            }
            // ball, strike, out 판별
            int ballC = 0;
            int strikeC = 0;
            for(int row = 0; row < RAND_NUM; row++){
                if(user_num[row] == computer_num[row]){
                    //strike
                    strikeC++;
                }else{
                    for(int col = 0; col < RAND_NUM; col++){
                        //ball
                        if(user_num[col] == computer_num[row]){
                            ballC++;
                        }
                    }
                }
            }
            if(ballC == 0 && strikeC == 0){
                outC++;
                System.out.println("out : 아웃 "+ outC +"번");
            }
            if(strikeC >= 1){
                System.out.print(strikeC +" strike ");
                // 1) win : 컴퓨터가 발생한 랜덤 값을 다 맞춘 경우 
            }
            if(ballC >= 1){
                System.out.println(ballC+" ball");
            }
            // 게임 조건 확인 후 그에 따른 결과 실행
            
            // 2) lose : 게임 횟수가 5회이상 또는 Strike out 2회 이상
            gameC++;

            if(strikeC == 3){
                System.out.println("");
                System.out.println("축하합니다. 이겼습니다.");
                for(int index = 0; index < computer_num.length; index++){
                    result += (computer_num[index] + " "); 
                }
                System.out.println(result + "입니다.");
                break;
            }
            if(gameC >= 5 || outC == 2){
                if(gameC >= 5)
                System.out.println("게임횟수 초과");
                
                // 결과출력
                System.out.println("아까비~~~졌네용..");
                    for(int index = 0; index < computer_num.length; index++){
                        result += (computer_num[index] + " "); 
                    }
                    System.out.println(result + "입니다.");
                    break;
            }
        }
        scn.close();
    }
}

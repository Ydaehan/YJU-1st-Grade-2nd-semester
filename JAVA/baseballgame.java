import java.util.Scanner;
public class baseballgame {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        // 야구게임만들기
        // 컴퓨터에 저장될 배열의 변수 생성
        final int RAND_NUM = 3;
        int computer_num[] = new int[RAND_NUM];
        // 저장될 배열의 초기값을 -1로 설정 
        for(int count = 0; count < RAND_NUM; count++){
            computer_num[count] = -1;
        }
        
        // 유저입력을 저장할 배열의 변수 생성
        int user_num[] = new int[RAND_NUM];
        String result = "정답은 : ";        
        int randnum = 0;

        // 중복되지 않은 0~9 사이 정수를 3개 생성 math.random()
        for(int row = 0; row < RAND_NUM; row++){
            randnum = (int)(Math.random()*10);
            for(int col = 0; col < RAND_NUM; col++){
                if(randnum == computer_num[col]){
                    randnum = (int)(Math.random()*10);
                    col = -1;
                }
            }
            computer_num[row] = randnum;
            result += (computer_num[row] + " ");
            //System.out.println(computer_num[row]);
        }
        result += "입니다.";


        int inputNum = 0;
        int outCount = 0;
        int tryCount = 1;
        while(true){
            // 배열 초기화
            for(int count = 0; count < RAND_NUM; count++){
                user_num[count] = -1;
            }
            System.out.println("시도횟수: " + tryCount);
            int strikeCount = 0;
            int ballCount   = 0;
            // 키보드로 부터 정수 3개 입력 받아 strike, ball, out 판정
            System.out.println("정수 3개를 입력하세용~~~^__^ ( 0 ~ 9 사이 정수 )");
            for(int row = 0; row < computer_num.length; row++){
                inputNum = scn.nextInt();
                for(int col = 0; col < computer_num.length; col++){
                    if(inputNum == user_num[col] || inputNum < 0 || inputNum > 9){
                        if(inputNum < 0 || inputNum > 9)
                            System.out.println("잘못입력하셨습니다. 0 ~ 9 사이 수를 입력해 주십시오.");
                        else
                            System.out.println("이미 입력한 수 입니다. 다시 입력해주십시오.");
                            
                        inputNum = scn.nextInt();
                        col = -1;
                    }
                }
                user_num[row] = inputNum;
            }
            for(int i = 0; i < RAND_NUM; i++){
                System.out.println(computer_num[i] + " | " + user_num[i]);
            }

            // strike , ball , out  판별
            for(int row = 0; row < computer_num.length; row++){
                if(user_num[row] == computer_num[row])
                    strikeCount++;
                else{
                    for(int col = 0; col < computer_num.length; col++){
                        if(user_num[row] == computer_num[col])
                            ballCount++;
                    }
                }
            }
            if(strikeCount == 0 && ballCount == 0){
                outCount++;
                System.out.println("Out: 아웃" + outCount + "번");
            }else if(strikeCount > 0){
                System.out.print(strikeCount + " strike");
            }else{
                System.out.println(ballCount + " ball");
            }
            System.out.println("");
            System.out.println("=====================================");
            
            // 종료
            // 시도횟수 >= 5 or strike out == 2
            tryCount++;
            // 맞추면 win
            if(strikeCount == 3){
                System.out.println("축하합니다. 승리하셨습니다.");
                System.out.println(result); 
                break;
            }

            if(tryCount >= 5 || outCount == 2){
                if(tryCount >= 5)
                    System.out.println("게임 횟수 초과");
                System.out.println("아까비~~~졌네용..");
                System.out.println(result);
                break;
            }
            
            
        }
        scn.close();
    }
    
}

import java.util.Scanner;
public class histPractice {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        System.out.println("배열의 개수를 입력하세요.");
        int inputFullIndex = scn.nextInt();
        while(inputFullIndex < 1 || inputFullIndex > 100){
            System.out.println("1이상의 값을 입력하세요.");
            inputFullIndex = scn.nextInt();
        }
        
        int randArray[] = new int[inputFullIndex];
        for(int i = 0; i < randArray.length; i++){
            int randNum = (int)(Math.random()*101 - 50);
            for(int j = 0; j < randArray.length; j++){
                if(randNum == randArray[j]){
                    randNum = (int)(Math.random()*101 - 50);
                    j = -1;
                }
            }
            
        }
        
        System.out.println("배 열 의\t개수 : " + inputFullIndex);

        scn.close();   
    }
}

public class myRotto {
    public static void main(String[] args) {
        // 로또 1 ~ 45 사이 중복 되지 않은 수 6개 랜덤 값
        // Math.random() => 난수값 호출 범위-> 0 <= a <= 1 의 실수값으로 return
        int rotto[] = new int[6];                          
        int num = 0;
        for(int i = 0; i < rotto.length; i++){
            num = (int)((Math.random() * 45 )+ 1);          // 1 ~ 45 사이 난수
            // 로또 배열 내 중복값 처리
            for(int j = 0; j < i ; j++){
                if(rotto[j] == num){                        // rotto 의 j 번째 와 num 의 값이 같으면 
                    num = (int)((Math.random() * 45 )+ 1);  // 새로 num 값을 받고
                    j = -1;                                 // searching 할 index 값을 -1 로 지정하여 다시 0부터 확인
                }
            }
            rotto[i] = num; 
        }
        for(int s = 0; s < rotto.length ; s++)
            System.out.print(rotto[s]+" ");
    }
}

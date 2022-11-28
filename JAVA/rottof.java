public class rottof {
    public static void main(String[] args) {
        // 1 ~ 45 rotto
        // 중복 x
        final int NUM_OF_ARRAY = 6; // 횟수 같은 상수형은 이름을 대문자로 선언함
        int rotto[] = new int[NUM_OF_ARRAY];
        for(int i = 0; i < NUM_OF_ARRAY; i++){
            int randnum = (int)((Math.random()*45)-1);
            // 중복 처리 검사
            for(int j = 0; j < i; j++){
                // 중복 값 발견
                if(rotto[j] == randnum){
                    randnum = (int)((Math.random()*45)-1);
                    j = -1;
                }
            }
            rotto[i] = randnum;
        }
        for(int result = 0 ; result < NUM_OF_ARRAY; result++){
            System.out.print(rotto[result]+" ");
        }
    }
}

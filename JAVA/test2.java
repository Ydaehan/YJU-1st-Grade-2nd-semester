public class test2 {
    public static void main(String[] args) {
        // for 문을 활용하여 다음과 같이 출력하는 프로그램 작성
        // for 문의 사용 개수는 제한 x (두 개 이상 사용 가능)
        // 반드시 for 문을 사용하여 알파벳을 연속적으로 출력, 하드코딩 시 점수 x
        char alpha;
        int count = 0;
        for(alpha = 'a'; alpha <= 'z'; alpha++){
            if(count % 3 == 0){
                System.out.print(alpha);
            }
            count ++;
        }
        System.out.println("");
        for(alpha = 'Z'; alpha >= 'A'; alpha--){
            System.out.print(alpha);
        }
    }
}

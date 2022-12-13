
public class ArrayPractice2 {
    public static void main(String[] args) {
        // 3행 3열짜리 문자열 배열을 선언 및 할당하고 인덱스 
        // 0행 0열부터 2행 2열까지 차례대로 접근하여 
        // “(0, 0)”과 같은 형식으로 저장 후 출력하세요.

        String bar[][] = new String[3][3];
        int i = 0;
        int j = 0;
        
        for(i = 0; i < bar.length; i++){
            for(j = 0; j < bar[i].length; j++){
                String result = "(" + i + "," + j + ")";
                bar[i][j] = result;
            }
        }

        for(int d = 0; d < bar.length; d++){
            for(int c = 0; c < bar[d].length; c++){
                System.out.print(bar[d][c] + "\t");
            }
            System.out.println("");
        }
    }
}

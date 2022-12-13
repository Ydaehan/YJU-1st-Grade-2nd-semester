public class ArrayPractice {
    public static void main(String[] args) {
        // // 2 by 4 matrix
        // char bar[][] = {{'k','i','n','g'},{'p','o','l','l'}};//= new char[2][4];
        
        // // bar[0][0] = 'k';
        // // bar[0][1] = 'i';
        // // bar[0][2] = 'n';
        // // bar[0][3] = 'g';
        // // bar[1][0] = 'p';
        // // bar[1][1] = 'o';
        // // bar[1][2] = 'l';
        // // bar[1][3] = 'l';
        // for(int i = 0; i < 2 ; i++){
        //     for(int j = 0; j < 4; j++){
        //         System.out.print(bar[i][j] + "\t");
        //     }
        //     System.out.println(" ");
        // }
        int bar[][] = {{3,4,5,2},{6,1,7,8}}; 
        int par[] = new int[8];
        int c = 0;
        int sortingNumber = 0;
        for(int a = 0 ; a < bar.length; a++){
            for(int b = 0 ; b < bar[a].length; b++,c++){
                par[c] = bar[a][b];
                System.out.print(par[c] + " ");
            }
            System.out.println("");
        }
        
        for(int d = 0; d < par.length - 1; d++){
            sortingNumber = par[d];
            if(par[d + 1] < sortingNumber){
                par[d] = par[d + 1];
                par[d + 1] = sortingNumber;
                d = -1;
            }
        }
        for(int e = 0; e < par.length ; e++){
            System.out.print(par[e] + " ");
        }
        

        

    }
}

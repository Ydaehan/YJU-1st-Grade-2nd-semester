public class graphExam {
    public static void main(String[] args) {
        // 배열 전체를 기준으로 최대,최소,중간 값을 출력하라.
        
        final int ROWNUM = 5;
        final int COLNUM = 5;

        int randArray[][] = new int [ROWNUM][COLNUM];

        // 1 ~ 50 사이의 중복되지 않은 정수형 난수
        // 25개를 선택하여 2차원 배열에 저장
        int randNum = 0;
        for(int row = 0; row < randArray.length; row++){
            for(int col = 0; col < randArray[row].length; col++){
                randNum = (int)(Math.random()*50 + 1);
                for(int checkRow = 0; checkRow < randArray.length; checkRow++){
                    for(int checkCol = 0; checkCol < randArray[checkRow].length; checkCol++){
                        if(randNum == randArray[checkRow][checkCol]){
                            randNum = (int)(Math.random()*50 + 1);
                            checkRow = -1;
                            break;
                        }
                    }
                }
                randArray[row][col] = randNum;
            }
        }
        
        // 각 열, 행 별 최대, 최소, 중간 값을 찾아 출력하라.
        // - 중간 값 : 데이터들을 크기순으로 배열 했을 때 전체의 중앙에 위치하는 수
        
        // 정렬 전 배열 의 값 출력 및 저장
        for(int i = 0; i < randArray.length; i++){
            for(int j = 0; j < randArray[i].length; j++){
                System.out.print(randArray[i][j] + "\t");
                randArray[i][j] = randArray[i][j];
            }
            System.out.println("");
        }
        System.out.println("");



        // 열 의 최소값 최대값 중간값 출력
        int min = 0;
        int max = 0;

        System.out.println("열");
        // 열의 최소값 출력
        System.out.print("최소값 ");
        for(int col = 0; col < COLNUM; col++){
            min = randArray[0][col];
            for(int row = 0; row < ROWNUM; row++){
                if(min > randArray[row][col]){
                    min = randArray[row][col];
                }
            }
            System.out.print(min + "\t");
        }
        System.out.println("");
        // 열의 최대값 출력
        System.out.print("최대값 ");
        for(int col = 0; col < COLNUM; col++){
            max = randArray[0][col];
            for(int row = 0; row < ROWNUM; row++){
                if(max < randArray[row][col]){
                    max = randArray[row][col];
                }
            }
            System.out.print(max + "\t");
        }

        System.out.println("");
        // 열의 값을 받아와서 정렬
        System.out.print("중간값 ");
        int colSort = 0;
        for(int i = 0; i < ROWNUM; i++){
            int rowArray[] = new int[ROWNUM];
            for(int j = 0; j < ROWNUM; j++){
                rowArray[j] = randArray[j][i];
            }
            for(int k = 0; k < rowArray.length - 1; k++){
                colSort = rowArray[k];
                if(colSort > rowArray[k + 1]){
                    rowArray[k] = rowArray[k + 1];
                    rowArray[k + 1] = colSort;
                    k = -1;
                }
            }
            // 열의 중간값
            System.out.print(rowArray[ROWNUM/2] + "\t");
        }


        System.out.println("");
        System.out.println("");
        System.out.println("행");
        // 행 의 최소값 출력
        System.out.print("최소값 ");
        for(int row = 0; row < COLNUM; row++){
            min = randArray[row][0];
            for(int col = 0; col < ROWNUM; col++){
                if(min > randArray[row][col]){
                    min = randArray[row][col];
                }
            }
            System.out.print(min + "\t");
        }
        System.out.println("");

        // 행 의 최대값 출력
        System.out.print("최대값 ");
        for(int row = 0; row < COLNUM; row++){
            max = randArray[0][row];
            for(int col = 0; col < ROWNUM; col++){
                if(max < randArray[row][col]){
                    max = randArray[row][col];
                }
            }
            System.out.print(max + "\t");
        }

        System.out.println("");
        // 행 의 중간값
        // 행의 값을 받아와서 정렬
        System.out.print("중간값 ");
        int rowSort = 0;
        for(int i = 0; i < ROWNUM; i++){
            int rowArray[] = new int[ROWNUM];
            for(int j = 0; j < ROWNUM; j++){
                rowArray[j] = randArray[i][j];
            }
            for(int k = 0; k < rowArray.length - 1; k++){
                rowSort = rowArray[k];
                if(rowSort > rowArray[k + 1]){
                    rowArray[k] = rowArray[k + 1];
                    rowArray[k + 1] = rowSort;
                    k = -1;
                }
            }
            // 행 의 중간값
            System.out.print(rowArray[ROWNUM/2] + "\t");
        }


        // 전체의 최소 최대 중간값
        // 전체 정렬
        int sortingNum = 0;
        int endIndexNum = 0;
        for(int row = 0 ; row < ROWNUM; row++){
            for(int col = 0; col < COLNUM; col++){
                for(int sortingRow = 0; sortingRow < randArray.length; sortingRow++){
                    for(int sortingCol = 0; sortingCol < randArray[sortingRow].length - 1; sortingCol++){
                        sortingNum = randArray[sortingRow][sortingCol];
                        if(sortingNum > randArray[sortingRow][sortingCol + 1]){
                            randArray[sortingRow][sortingCol] = randArray[sortingRow][sortingCol + 1];
                            randArray[sortingRow][sortingCol + 1] = sortingNum;
                        }
                        if(sortingRow != ROWNUM - 1 && (sortingCol == randArray[sortingRow].length - 2) && randArray[sortingRow][sortingCol + 1] > randArray[sortingRow + 1][0]){
                            endIndexNum = randArray[sortingRow][sortingCol + 1];
                            randArray[sortingRow][sortingCol + 1] = randArray[sortingRow + 1][0];
                            randArray[sortingRow + 1][0] = endIndexNum; 
                        }
                    }
                }
            }
        }
        System.out.println("");
        System.out.println("");

        System.out.println("전체");
        // 전체의 최소값
        System.out.println("최소값 " + randArray[0][0]);
        // 전체의 최대값
        System.out.println("최대값 " + randArray[ROWNUM-1][COLNUM-1]);
        // 전체의 중간값
        System.out.println("중간값 " + randArray[(ROWNUM-1)/2][(COLNUM-1)/2]);


        // 정렬 후 배열 의 값 출력
        for(int i = 0; i < randArray.length; i++){
            for(int j = 0; j < randArray[i].length; j++){
                System.out.print(randArray[i][j] + "\t");
            }
            System.out.println("");
        }
        System.out.println("");
    }
}

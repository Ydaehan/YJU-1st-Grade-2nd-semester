public class arrayPractice3 {
    public static void main(String[] args) {
        // 랜덤함수를 이용 1- 50 사이 정수 중복x 25개 
        // 2차원 배열에 저장 행/열/전체 의 최대/최소/중간값
        // 찾기
        
        final int ROW  = 5;
        final int COL  = 5;
        int originRandArray[][] = new int[ROW][COL];
        int randValue = 0;

        // 랜덤함수로 1~50 난수 25개 뽑기
        for(int rowNum = 0; rowNum < originRandArray.length; rowNum++){
            for(int colNum = 0; colNum < originRandArray[rowNum].length; colNum++){
                randValue = (int)(Math.random()*50 + 1);
                // 중복처리
                for(int dupRow = 0; dupRow < originRandArray.length; dupRow++){
                    for(int dupCol = 0; dupCol < originRandArray[dupRow].length; dupCol++){
                        if(originRandArray[dupRow][dupCol] == randValue){
                            randValue = (int)(Math.random()*50 + 1);
                            dupRow = -1;
                            break;
                        }
                    }
                }
                originRandArray[rowNum][colNum] = randValue;
                System.out.print(randValue+"\t");
            }
            System.out.println("");
        }
        System.out.println("");

        
        System.out.println("열");
        // 열의 최소 최대 중간값 출력
        int colArray[] = new int[COL];
        System.out.print("최소값:\t");
        for(int col = 0; col < originRandArray.length; col++){
            // colArray[] 1D Array 에 한 열 씩 저장
            for(int minCol = 0; minCol < originRandArray[col].length; minCol++){
                colArray[minCol] = originRandArray[minCol][col];
            }

            int min = colArray[0];
            for(int checkCol = 0; checkCol < colArray.length - 1; checkCol++){
                if(colArray[checkCol] < min){
                    min = colArray[checkCol];
                }
            }
            System.out.print(min + "\t");
        }
        System.out.println("");


        // 열의 최대값
        System.out.print("최대값:\t");
        for(int col = 0; col < originRandArray.length; col++){
            // colArray[] 1D Array 에 한 열 씩 저장
            for(int maxCol = 0; maxCol < originRandArray[col].length; maxCol++){
                colArray[maxCol] = originRandArray[maxCol][col];
            }

            int max = colArray[0];
            for(int checkCol = 0; checkCol < colArray.length - 1; checkCol++){
                if(colArray[checkCol] > max){
                    max = colArray[checkCol];
                }
            }
            System.out.print(max + "\t");
        }
        System.out.println("");


        // 열의 중간값
        System.out.print("중간값: ");
        for(int col = 0; col < originRandArray.length; col++){
            // colArray[] 1D Array 에 한 열 씩 저장
            for(int midCol = 0; midCol < originRandArray[col].length; midCol++){
                colArray[midCol] = originRandArray[midCol][col];
            }

            int sortingValue = 0;
            for(int colMid = 0; colMid < colArray.length - 1; colMid++){
                sortingValue = colArray[colMid];
                if(sortingValue > colArray[colMid + 1]){
                    colArray[colMid] = colArray[colMid + 1];
                    colArray[colMid + 1] = sortingValue;
                }
            }

            System.out.print(colArray[COL/2]+ "\t");
        }
        System.out.println("");
        System.out.println("");


        System.out.println("행");
        // 행의 최소 최대 중간값 출력
        int rowArray[] = new int[ROW]; 
        // 최소 최대 중간값
        System.out.println("최소값\t최대값\t중간값");
        for(int row = 0; row < originRandArray.length; row++){
            // 행의 최소값과 최대값
            for(int maxCol = 0; maxCol < originRandArray[row].length; maxCol++){
                rowArray[maxCol] = originRandArray[row][maxCol]; // 1차원 배열에 한 행 씩 저장
            }

            // 행의 최소
            int min = rowArray[0];
            for(int checkMin = 0; checkMin < rowArray.length; checkMin++){
                if(rowArray[checkMin] < min){
                    min = rowArray[checkMin];
                }       
            }
            System.out.print(min + "\t");


            // 행의 최대
            int max = rowArray[0];
            for(int checkMax = 0; checkMax < rowArray.length; checkMax++){
                if(rowArray[checkMax] > max){
                    max = rowArray[checkMax];
                }       
            }
            System.out.print(max + "\t");
            
            
            // 행의 중간
            int sortingValue = 0;
            for(int rowMid = 0; rowMid < rowArray.length - 1; rowMid++){
                sortingValue = rowArray[rowMid];
                if(sortingValue < rowArray[rowMid + 1]){
                    rowArray[rowMid] = rowArray[rowMid + 1];
                    rowArray[rowMid + 1] = sortingValue;
                    rowMid = -1;
                }
            }
            System.out.println(rowArray[ROW/2]);
        }
        System.out.println("");

        // 전체의 최대 최소 중간값
        int allArrayValue[] = new int[ROW*COL];


        // 전체를 1D Array에 저장
        int index = 0;
        for(int allRow = 0; allRow < originRandArray.length; allRow++){
            for(int allCol = 0; allCol < originRandArray[allRow].length; allCol++){
                allArrayValue[index] = originRandArray[allRow][allCol];
                index++;
            }
        }
        int nowValue = 0;
        for(int sortingAll = 0; sortingAll < allArrayValue.length - 1; sortingAll++){
            nowValue = allArrayValue[sortingAll];
            if(nowValue > allArrayValue[sortingAll + 1]){
                allArrayValue[sortingAll] = allArrayValue[sortingAll + 1];
                allArrayValue[sortingAll + 1] = nowValue;
                sortingAll = -1;
            }
        }

        System.out.println("전체");
        System.out.println("최소값 : " + allArrayValue[0]);
        System.out.println("최대값 : " + allArrayValue[allArrayValue.length - 1]);
        System.out.println("중간값 : " + allArrayValue[allArrayValue.length / 2]);
    }
}

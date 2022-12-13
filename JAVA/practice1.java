// import java.util.Scanner;
public class practice1 {
    public static void main(String[] args) {
        // continue, break
        // continue : 계속하다.
        // break : 멈추다, 탈출하다.
        /*
        Data structure (자료 구조)
        배열 이란? (Array)
        같은 타입의 여러 변수를 하나의 묶음으로 다루는 것
        많은 양의 값(데이터)을 다룰 때 유용
        배열의 각 요소는 서로 연속적이다.
         */
        // 5명 학생에 대한 성적을 입력 받아 평균을 출력하라
        // Scanner scn = new Scanner(System.in);
        // // 여러개의 데이터를 하나의 집합으로 만들면 어떨까? -> 배열
        // int std[] = new int[5];
        // int sum = 0;
        // for(int i = 0; i < std.length; i++){
        //     std[i] = scn.nextInt();
        //     sum += std[i];
        // }
        // float avg = sum / 5.0f;
        // System.out.println(avg);
        /*
         배열 : 같은 자료형의 변수를 메모리 공간상에 
         나열하여 자료를 관리하는 방법
         배열 내의 각각의 항목을 원소(Element) 라고 한다.
         각각 원소의 자료형은 다 같은 자료형이여야 한다.
         */
        // 일반 변수와 배열의 차이점
        // int bar = 5; => 메모리(ram) 안에 4byte 짜리 공간이 만들어지고
        // 이름은 bar 인 메모리 공간이 할당 후 값이 정수 5가 들어감

        // 1st => int foo[];  int[] foo; 도 가능하다.  C언어에서는 전자만 사용
        // => 메모리상에 4byte 짜리 공간이 만들어 지고 이름은 foo 인 메모리공간이 할당됨
        // long pos []; -> 자료형이 long 임에도 pos라는 이름의 4byte 공간이 만들어짐
        // byte kal []; -> 자료형이 byte 임에도 kal이라는 이름의 4byte 공간이 만들어짐
        // 각 배열의 첫번째 원소의 주소값을 저장하기 때문에 운영체제(JVM)에서 32bit 사용하기때문에
        // Java Virtual Machine
        // 주소값의 크기는 32bit = 4byte 이기때문에 모두 4byte 공간이 만들어짐

        // 0 1 2 3  - 4개의 변수를 가지는 배열을 만들고 싶다 
        // -> new int[4]; => 메모리 상에 4byte 짜리 정수형을 담을수 있는 공간이
        // 총 16byte 가 연속적으로 만들어짐 원소 하나당 = 4byte

        // ex) int foo[];
        // foo = new int[4]; -> [n] - n 은 정수 1부터 시작

        // 배열의 원소 번호는 0 번부터 시작
        // double bar []; - 메모리 공간에 4byte 짜리 bar 가 만들어짐
        // new double[3]; - double = 8byte 짜리 - 메모리 공간에 8byte 짜리 실수형을 담을수
        // 있는 공간이 총 24byte가 연속적으로 만들어짐 원소 하나당 = 8byte
        // bar[2] = 0.9; => 0x200 / 0x200 / 0.9    두번 쉬프트(뛰어넘고)하고 3번째 원소에 update(수정) 집어넣기
        // bar[0] = 0.1; => 0.1 / 0x200 / 0.9      배열은 데이터를 차례로 넣을 필요없다.
        // bar[1] = 0.5; => 0.1 / 0.5 / 0.9
        // bar[1] = bar[2]; => 0.1 / 0.9 / 0.9
        
        // int bar[]; int[]foo; 둘다 사용가능
        // 배열변수 bar 선언 / 배열변수 foo 선언
        // foo = new int[10];  배열의 주소값을 0x900 이라 했을때 foo의 값은 0x900 이 됨
        // bar = foo;  bar 에 foo 값을 넣어라 -> bar -> 0x900 이 됨
        // foo[0] = 20; foo 에 20을 넣어도 bar 와 foo 가 가르키는 배열이 0x900
        // System.out.println(bar[0]); 
        // 결과값 = 20       
        
        // variable - primitive (int / float / char / boolean) - 원시적 / 그대로의 값을 변수에 저장
        //          - reference (String / Array) - 주소값을 저장하기 위한 변수
        //          - python 에서는 reference 사용 

        // 배열의 변수가 필요한 이유
        // 배열의 변수가 없으면 배열을 불러 올 수 없음
        // 사용하고자 하는 배열을 가르키기 위해서

        // 변수의 동작 모드
        // 1. GET 값 읽어오기
        // 2. SET 값 저장하기

        // char bar[] = new char[2]; 에서
        // new -> 메모리 상의 객체를 생성  -> 첫번째 원소의 메모리 주소값을 들고 옴
        // shifting 알고리즘 = 자료형사이즈 * index
        
        // 배열을 초기화 하는 방법
        // 초기화를 하지 않으면 원소의 값은 모두 0으로 초기값 설정됨
        // 1. literal constant (리터럴 상수)
        // int foo[] = {10, 20, 30, 40};
        // char foo[] = {'h','e','l','l','o'}
        // for(int i = 0 ; i < foo.length ; i++){
        //     System.out.print(foo[i]);
        // }
        // 2. for loop;
        // final int NUM_OF_WEIGHT = 6; 상수화
        // double weight[] = new double[NUM_OF_WEIGHT];
        
        // for ( int i = 0 ; i < weight.length ; i++){
        //     weight[i] = Math.random();            
        // }
        // for ( int j = 0 ; j < weight.length ; j++){
        //     System.out.println(weight[j]);
        // }
        //scn.close();
        // --------------복습--------------------
        // final int NUM_OF_ELEMENT = 3; //변수 -> 상수 상수의 이름은 모두 대문자로 쓴다 <약속>
        // int bar[] = new int[NUM_OF_ELEMENT];
        // // 10, 20, 30
        // // loop
        // // java 에서 array는 객체[object] 로 인식한다. 
        // for(int i = 0, j = 10; i < bar.length; i++, j += 10){
        //     // 3번 반복, i -> 0, 1, 2
        //     bar[i] = j;
        // }

        // for(int i = 0; i < bar.length; i++){
        //     System.out.print(bar[i] + "\t");
        // }

        // int bar[] = {2, 3, 4}; // reference variable 참조형 변수
        
        // int foo[]; // primitive variable 원시적 변수
        // -------------- 여기까지 일차원 배열 --------------- 
        // 2차원 배열

        // scalar -> 한개의 값                      -> primitive variable
        // vector -> 일차원                         -> 1D Array
        // Matrix -> 이차원                         -> 2D Array
        // 관계형 데이터 베이스의 저장 방법과 유사
        // 이차원 배열에서의 좌표 체계 
        // 2번째 행의 index 가 3번째의 좌표값        -> (1, 3)
        // Tensor -> 삼차원 이상 [다차원 배열]       -> 3D >= Array
        // ROW BY COLUMN -> ROW x COLUMN 배열
        
        // 이차원 배열 생성 과정
        // 배열의 변수 선언
        // int bar[][]; -> []은 하나의 차원 / 이차원에서의 배열의 변수 선언
        // 배열의 원소 Element 할당
        // new int [4][4]; [ROW][COL];
        // 3. Chainning 배열 변수와 할당된 배열
        // bar = new int [4][4];

        // 2차원 배열의 초기화
        // int foo [][] = { {1, 2, 3} , {4, 5, 6}, {7, 8, 9}};
        // int foo[][] = new int[3][3];
        // 각 행에서 각 열로 돌아야하기때문에 loop를 2번 써야한다
        // ROW
        // int count = 1;
        // for(int i = 0; i < foo.length; i++){
        //     // COLUMN
        //     for(int j = 0; j < foo[i].length; j++){
        //         foo[i][j] = count;
        //         count++;
        //     }
        // }

        // // print
        // for(int i = 0; i < foo.length; i++){
        //     // COLUMN
        //     for(int j = 0; j < foo[i].length; j++){
        //         System.out.print(foo[i][j] + "\t");
        //     }
        //     System.out.println("");
        // }

        // java 태생 자체 oop function 대신 method 와 생성자가 있다
        // 이것은 Class 개념을 알아야 사용 가능

        // 3차원 이상 <Tensor 3D Array>
        // 3차원 이기 때문에 브라켓은 3개 [][][]
        // [2][3] 짜리 2 by 3 2D Array를 N개 생성할때 ->
        // int foo[][][] = new int[N][3][4]; 처럼 생성
        // 28 by 28 2D Array * 3 을 선언 <3차원으로>
        // int bar[][][] = new int[3][28][28];

        // 3차원 배열의 초기화
        // 1. 리터럴 상수
        // [2][2][2]
        // int foo[][][] = new int[][][]{ { {1,2},{3,4} },{ {5,6},{7,8} }};
        // 2. loop
        // for 문 3개 필요
        
        // N번째 Matrix
        // for(int i = 0 ; i < foo.length; i++){
        //     // ROW
        //     for(int j = 0 ; j < foo[i].length; j++){
        //         // COL
        //         for(int k = 0 ; k < foo[i][j].length; k++){ 
        //             System.out.print(foo[i][j][k] + "\t");
        //         }
        //         System.out.println("");
        //     }
        //     System.out.println("====================");
        // }
    }
}

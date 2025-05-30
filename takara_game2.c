#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAKARA_NUM 8  //宝の数
#define SIZE 10       //フィールドの1辺のサイズ
#define MAX(a,b) ((a) > (b) ? (a) :(b))
#define MIN(a,b) ((a) < (b) ? (a) :(b))

//aからbの範囲の乱数発生
int random_number(int a, int b)
{
    int c;

    c = rand() % (b - a + 1) + a;
    return(c);
}

// takaraに宝をTAKARA_NUM　個セットする
void set_treasure(int takara[SIZE][SIZE])
{
    int x, y, i;
    time_t t;

    //乱数のシードを指定する
    time(&t);
    srand((unsigned int)t);

    for (i = 0; i < TAKARA_NUM; i++) {
        do {
            x = random_number(0, 9);
            y = random_number(0, 9);
        } while (takara[y][x] == -2);
    
        takara[y][x] = -2;
    }
}

//8近傍カウント
int count(int takara[SIZE][SIZE], int x, int y)
{
    int TAKARA = 0;

    if (y > 0 && x < SIZE - 1) {
        if ((takara[y - 1][x + 1] == -2) || (takara[y - 1][x + 1] == -3))
            TAKARA++;
    }
    if (x < SIZE - 1) {
        if ((takara[y][x + 1] == -2) || (takara[y][x + 1] == -3))
            TAKARA++;
    }
    if (y < SIZE - 1 && x < SIZE - 1) {
        if ((takara[y + 1][x + 1] == -2) || (takara[y + 1][x + 1] == -3))
            TAKARA++;
    }
    if (y > 0) {
        if ((takara[y - 1][x] == -2) || (takara[y - 1][x] == -3))
            TAKARA++;
    }
    if (y < SIZE - 1) {
        if ((takara[y + 1][x] == -2) || (takara[y + 1][x] == -3))
            TAKARA++;
    }
    if (y > 0 && x > 0) {
        if ((takara[y - 1][x - 1] == -2) || (takara[y - 1][x - 1] == -3))
            TAKARA++;
    }
    if (x > 0) {
        if ((takara[y][x - 1] == -2) || (takara[y][x - 1] == -3))
            TAKARA++;
    }
    if (y < SIZE - 1 && x > 0) {
        if ((takara[y + 1][x - 1] == -2) || (takara[y + 1][x - 1] == -3))
            TAKARA++;
    }

    return TAKARA;
}

//ディスプレイ表示
void display(int takara[SIZE][SIZE], int x, int y, int counter, int i)
{
    int display_x, display_y;
    
    printf("Phase = %d\n", counter);
    printf("Treasures left = %d\n", 8 - i);

    printf("    a   b   c   d   e   f   g   h   i   j  \n");
    for (display_y = 0; display_y < SIZE; display_y++) {
        printf(" %d", display_y);
        for (display_x = 0; display_x < SIZE; display_x++) {
            if (takara[display_y][display_x] >= 0) {
                printf("  %d ", takara[display_y][display_x]);
            }
            else if (takara[display_y][display_x] == -3) {
                printf(" $%d ", count(takara, display_x, display_y));
            }
            else {
                printf("  + ");
            }
        }
        printf("%d \n", display_y);
    }
    printf("    a   b   c   d   e   f   g   h   i   j  \n");
}

void display_ans(int takara[SIZE][SIZE], int x, int y)
{
    int display_x, display_y;
    
    printf("    a   b   c   d   e   f   g   h   i   j  \n");
    for (display_y = 0; display_y < SIZE; display_y++) {
        printf(" %d", display_y);
        for (display_x = 0; display_x < SIZE; display_x++) {
            if (takara[display_y][display_x] >= 0) {
                printf("  %d ", count(takara, display_x, display_y));
            }
            else if (takara[display_y][display_x] == -3) {
                printf(" $%d ", count(takara, display_x, display_y));
            }
            else {
                printf("  %d ", count(takara, display_x, display_y));
            }
        }
        printf("%d \n", display_y);
    }
    printf("    a   b   c   d   e   f   g   h   i   j  \n");
}

void display_ans2(int takara[SIZE][SIZE], int x, int y)
{
    int display_x, display_y;
    
    printf("    a   b   c   d   e   f   g   h   i   j  \n");
    for (display_y = 0; display_y < SIZE; display_y++) {
        printf(" %d", display_y);
        for (display_x = 0; display_x < SIZE; display_x++) {
            if (takara[display_y][display_x] >= 0) {
                printf("  %d ", count(takara, display_x, display_y));
            }
            else if (takara[display_y][display_x] == -2) {
                printf(" $%d ", count(takara, display_x, display_y));
            }
            else {
                printf("  %d ", count(takara, display_x, display_y));
            }
        }
        printf("%d \n", display_y);
    }
    printf("    a   b   c   d   e   f   g   h   i   j  \n");
}

int main(void)
{    
    int takara[SIZE][SIZE];
    int x, y;
    int counter = 1;
    char MOJI2[10];
    int xx = 0;
    int yy = 0;
    int a = 0;
    int b = 0;
    int i = 0;
    
    // フィールドの初期化
    for (y = 0; y < SIZE; y++) {
        for (x = 0; x < SIZE; x++) {
            takara[y][x] = -1;
        }
    }

    random_number(a, b);
    set_treasure(takara);

    display(takara, x, y, counter, i);
    printf("ーーーーーーーーーーーーーーーーーーーーーー\n");
    //ゲーム開始
    while (1) {
        //display_ans2(takara, x, y);
        while (1) {
            printf("Input : ");
            scanf("%s", MOJI2);  // バッファオーバーフローの可能性あり
            if ((('a' <= MOJI2[0] && MOJI2[0] <= 'j') && ('0' <= MOJI2[1] && MOJI2[1] <= '9')) || (MOJI2[0] == 'q'))
            {
                break;
            }
            else {
                printf("正しい数値を入力してください\n");
            }
        }
        if (MOJI2[0] == 'q') {
            break;
        }
        xx = MOJI2[0] - 'a';
        yy = MOJI2[1] - '0';
        x = xx;
        y = yy;

        if (takara[yy][xx] == -2) {
            printf("GET!!\n");
            takara[yy][xx] = -3;
            i++;
        }
        else if (takara[yy][xx] == -3) {
            printf("その宝はすでに見つけています。\n別の値を入力してください。\n");
            counter--;
        }
        else if (takara[yy][xx] >= 0){
            printf("そこはすでに調べ終わっています。\n別の値を入力してください。\n");
            counter--;
        }
        else {
            takara[yy][xx] = count(takara, x, y);
        }
        if (i == 8) {
            printf("クリア！！\n");
            display_ans(takara, x, y);
            break;
        }
        
        display(takara, x, y, counter, i);

        counter++;
    }

    return 0;
}
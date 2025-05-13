#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAKARA_NUM 8  /* 宝の数 */
#define SIZE 10       /* フィールドの一辺のサイズ */

/* a から b の範囲の乱数発生 */
int random_number(int a, int b)
{
    int c;
    
    c = rand() % (b - a + 1) + a;
    return(c);
}

/* takara に宝を TAKARA_NUM 個セットする */
void set_treasure(int takara[SIZE][SIZE])
{
    int x, y, i;
    time_t t;
    
    /* 乱数のシードを指定する */
    time(&t);
    srand((unsigned int)t);
    
    for (i = 0; i < TAKARA_NUM; i++) {
        do {
            x = random_number(0, 9);
            y = random_number(0, 9);
        } while (takara[x][y] == 1);
        
        takara[x][y] = 1;
    }
}

/* グリッドを表示する */
void display_grid(int takara[SIZE][SIZE], int revealed[SIZE][SIZE])
{
    int i, j;
    
    printf("  a b c d e f g h i j\n");
    
    for (i = 0; i < SIZE; i++) {
        printf("%d ", i);
        for (j = 0; j < SIZE; j++) {
            if (revealed[j][i] == 1) {
                if (takara[j][i] == 1) {
                    printf("O ");
                } else {
                    printf("+ ");
                }
            } else {
                printf("+ ");
            }
        }
        printf("%d\n", i);
    }
    printf("  a b c d e f g h i j\n");
}

/* 入力を座標に変換する */
int convert_input(char *input, int *x, int *y)
{
    if (input[0] >= 'a' && input[0] <= 'j') {
        *x = input[0] - 'a';
    } else {
        return 0;
    }
    
    if (input[1] >= '0' && input[1] <= '9') {
        *y = input[1] - '0';
    } else {
        return 0;
    }
    
    return 1;
}

int main()
{
    int takara[SIZE][SIZE] = {0};
    int revealed[SIZE][SIZE] = {0};
    int treasures_left = TAKARA_NUM;
    int phase = 1;
    char input[3];
    int x, y, valid_input;
    
    /* 宝を設定 */
    set_treasure(takara);
    
    while (treasures_left > 0) {
        printf("Phase = %d\n", phase);
        printf("Treasures left = %d\n", treasures_left);
        
        /* グリッドを表示 */
        display_grid(takara, revealed);
        
        /* プレイヤーからの入力を受け取る */
        do {
            printf("Input : ");
            scanf("%2s", input);
            valid_input = convert_input(input, &x, &y);
            
            if (!valid_input) {
                printf("無効な入力です。a0～j9の形式で入力してください。\n");
            }
        } while (!valid_input);
        
        /* 既に開いたマスかチェック */
        if (revealed[x][y] == 1) {
            printf("既に確認済みのマスです。\n");
        } else {
            revealed[x][y] = 1;
            
            /* 宝を見つけたかチェック */
            if (takara[x][y] == 1) {
                printf("GET !!\n");
                treasures_left--;
            }
        }
        
        phase++;
    }
    
    /* 最終的なグリッドを表示 */
    printf("おめでとうございます！すべての宝を見つけました！\n");
    printf("Phase = %d\n", phase);
    printf("Treasures left = %d\n", treasures_left);
    display_grid(takara, revealed);
    
    return 0;
}
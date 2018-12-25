#include <stdio.h>
#include <conio.h>
#include <windows.h>
FILE *f;
int h[8][2] = {-2, 1, -1, 2, 1, 2, 2, 1, 2, -1, 1, -2, -1, -2, -2, -1}; 				//bien danh cho Ma Di Tuan
int daqua[100][100];
int x1, y1, m1, sc, dem = 0;

// ham kiem tra vi tri con ma co dung hay k

int ok(int u, int k) {
    if (u >= 1 && u <= k) return 1;	//1<u<8 tra ve dung
    else return 0;
}

void nhapdl() {
    printf("\nNhap so hang & so cot cua ban co : ");
    scanf("%d", &m1);
    do {
        printf("Nhap toa do hang ban dau X cua con ma (1<=X<=M) : ");
        scanf("%d", &x1);
    } while (!ok(x1, m1));
    do {
        printf("Nhap toa do cot ban dau Y cua con ma (1<=Y<=N) : ");
        scanf("%d", &y1);
    } while (!ok(y1, m1));
}

void khoitao() {
    sc = 0;				//bien dem = 0
    daqua[x1][y1] = 1;	//nuoc di dung
}

void xuat(int sc) {
    printf("----------------------------------------\n");
    printf("Cach thu %d de con ma di het ban co : \n", sc);
    for (int i = 1; i <= m1; i++) {
        for (int j = 1; j <= m1; j++)
            printf("%d    ", daqua[i][j]);
        printf("\n\n");
    }
}

void xuat1(int sc) {
    fprintf(f, "----------------------------------------\n");
    fprintf(f, "Cach thu %d de con ma di het ban co : \n", sc);
    for (int i = 1; i <= m1; i++) {
        for (int j = 1; j <= m1; j++)
            fprintf(f, "%d    ", daqua[i][j]);
        fprintf(f, "\n\n");
    }
}
//ma di tuan

void MaDiTuan(int u, int v, int c) {
    int uu, vv;
    if (c == m1 * m1) {
        sc++;								//tang bien dem
        xuat(sc);							//in ra man hinh cach ung vs sc
        xuat1(sc);
    } else {
        for (int i = 0; i <= 7; i++) {
            uu = u + h[i][0];
            vv = v + h[i][1];
            if (ok(uu, m1) && ok(vv, m1))	//neu vi tri hang & cot dung thi thuc hien
                if (!daqua[uu][vv]) {		//nuoc di sai thi thuc hien
                    daqua[uu][vv] = c + 1;	//nuoc di hop le
                    MaDiTuan(uu, vv, c + 1);//thuc hien nuoc di tiep theo
                    daqua[uu][vv] = 0;		//huy 1 nuoc di
                }
        }
    }
}
int main() {
    system("MODE CON COLS=100 LINES=59"); 							//thay doi kich thuoc khung cmd
    SetConsoleTitle("Nguyen Quoc Tan 15T2 - nqt.it.bk@gmail.com"); 	//doi ten file cmd
    printf("\n\t\t\t\tDO AN GIAI THUAT LAP TRINH C/C++ 2017");
    printf("\n\t\t\t\tNGUYEN QUOC TAN 15T2 MSSV: 102150131");
    printf("\n\t\t\t\t\tQUAY LUI & SAP XEP");
	printf("\n13.Bai toan Ma Di Tuan(Ban co 5x5 -> 8x8)");		
                f = fopen("MaDiTuan.txt", "w");
                nhapdl();
                khoitao();
                MaDiTuan(x1, y1, 1);
                printf("--------------------------------------------------------");
                printf("\nVay co tong cong %d cach de con ma di het ban co!(^_^)\n", sc);
                fprintf(f, "--------------------------------------------------------");
                fprintf(f, "\nVay co tong cong %d cach de con ma di het ban co!(^_^)", sc);
                fclose(f);    
}                

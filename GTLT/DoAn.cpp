#include <stdio.h>
#include <conio.h>
#include <windows.h>
#include <stdlib.h>  
#define abs(x) ((x)<0?(-(x)):(x))

FILE *f, *fp;
int n, k, x, cv,cv1, i, j; 																	//bien danh cho tim kiem, sap xep
int a[100], b[100], S[100] = {0}, s[100];
int c = 0, c1 = 0, c2 = 0, d = 0, d1 = 0, d11 = 0, d2 = 0, d22 = 0, d3 = 0, d33 = 0; 	//bien danh cho cau hinh to hop
int h[8][2] = {-2, 1, -1, 2, 1, 2, 2, 1, 2, -1, 1, -2, -1, -2, -2, -1}; 				//bien danh cho Ma Di Tuan
int daqua[100][100];
int x1, y1, m1, sc, dem = 0;
int a1[630]; 																			//bien Sudoku
int lastK;

//ham doi 2 so

void swap(int &a, int &b) {
    int t = a;
    a = b;
    b = t;
}
//sap xep chon

void SelectSort(int *a, int n) {							
    for (i = 0; i < n - 1; i++) {
        int t = i;
        for (j = i + 1; j < n; j++)	//a[j] lien ke a[i]
            if (*(a + t)>*(a + j))
                t = j; 				// tim t trong phantu con lai
        swap(*(a + t), *(a + i)); 	// doi cho neu tim thay
    }
}

//sap xep noi bot

void BubbleSort(int *a, int n) {
    for (i = 0; i < n; i++) 			
    {
        for (j = n - 1; j > i; j--)		// sap tu cuoi len dau
            if (*(a + j)<*(a + j-1))
                swap(*(a + j), *(a + j-1));
    }
}
//sap xep chen

void InsertSort(int *a, int n) {
    int t;
    for (i = 1; i < n; i++) {			//sap xep tu dau den cuoi
        j = i - 1;						//j tu 0 -> n-1
        t = *(a + i);
        while (t>*(a + j) && j >= 0) {	//thuc hien trong khi a[i]>a[j]
            *(a + j + 1) = *(a + j);	//chen a[j] vao mang
            j--;						//lui mang ve 1 vitri
        }
        *(a + j + 1) = t;				//chen t vao mang
    }
}
//doi cho truc tiep

void InterchangeSort(int *a, int n) {
    for (i = 0; i < n - 1; i++)				//sap xep tu dau den cuoi
        for (j = i + 1; j < n; j++)			//a[j] dung ke sau a[i]
            if (*(a + j)>*(a + i))			//neu a[j]>a[i] thi doi cho
                swap(*(a + i), *(a + j));
}
//shellsort giam dan

void ShellSort(int *a, int n, int *h, int k) {
    int step, i, j, x, len;
    for (step = 0; step < k; step++) {
        len = *(h + step);
        for (i = len; i < n; i++) {
            x = *(a + i);
            j = i - len; 					//a[j] dung ke truoc a[i] trong cung day con
            while (x<*(a + j)&&(j >= 0)) 	// sap xep day con chua x = pp chen truc tiep
            {
                *(a + j + len) = *(a + j);	//chen a[j] vao mang
                j -= len;
            }
            *(a + j + len) = x;
        }
    }
}

int Partition(int *a, int l, int r) {
    int p = *(a + l);						//p=a[0]
    int i = l + 1;							
    int j = r;
    while (1) {
        while (*(a + i) <= p && i < r)		//thuc hien trong khi a[0]>a[i] & i<n
            ++i;
        while (*(a + j) >= p && j > l)		//thuc hien trong khi a[j]>=a[0] & j>0
            --j;
        if (i >= j) {
            swap(*(a + j), *(a + l));
            return j;
        } else swap(*(a + i), *(a + j));
    }
}
//sap xep nhanh

void QuickSort(int *a, int l, int r) {
    if (r > l) {
        int p = Partition(a, l, r);
        QuickSort(a, l, p - 1);
        QuickSort(a, p + 1, r);
    }
}

void inputArray(int *a, int n) {
    for (int i = 0; i < n; i++) {
        //printf("a[%d]= ",i);
        //scanf("%d",&a[i]);
        *(a + i) = rand();					//random gia tri cua mang n phantu
    }
}

void PrintArray(int *a, int n) {
    for (i = 0; i < n; i++) {
        printf("%d ", *(a + i));
    }
}
//mo file

void openFile(int *a, int n) {
    f = fopen("output.txt", "r");
    n = 0;
    							// hoac while (feof(f) == 0)
    while (!feof(f)) {
        fscanf(f, "%d ", &a[n]);//doc gia tri tung so trong file
        n++;					//tang gia tri len
    }
    fclose(f);
    printf("\n\nMang mo tu file output.txt la:\n");
    PrintArray(a, n); 			//xuat mang vua doc
    printf("\n");
}
//in ra file

void creatFile(int *a, int n) {
    f = fopen("output.txt", "w");
    for (i = 0; i < n; i++)
        fprintf(f, "%d ", *(a + i)); //in noi dung ra file
    fclose(f);
}

int trienVong(int k) { 				//s[i] != s[k] moi cot chi co 1 con hau
    int i; 							//|i-k|!-s[i]-s[k] moi duong cheo chi co 1 hau
    for (i = 1; i < k; i++)
        if (*(s + k) == *(s + i) || abs(i - k) == abs(*(s + i) - *(s + k))) return 0;
    return 1;						//neu k co dieu kien nao sao thi moi tra ve 1
}
//in vi tri con Hau ra man hinh

int xepHau(int k) {
    int i;
    if (k == n + 1) {
        d1++;
        printf("\n%d: ", d1);								//in so luong		
        for (i = 1; i <= n; i++) printf("%d  ", *(s + i)); 	//in cach xepHau vi tri s[i]
        //printf("\n");
    } else for (i = 1; i <= n; i++) {
            *(s + k) = i;
            if (trienVong(k)) xepHau(k + 1); 				//neu trienVong thi thuc hien hang tiep theo
        }
}
//in vi tri con Hau ra file txt

int xepHau1(int k) {
    int i;
    if (k == n + 1) {
        d11++;
        fprintf(f, "\n%d: ", d11);
        for (i = 1; i <= n; i++) fprintf(f, "%d  ", *(s + i));
        //fprintf(f, "\n");
    } else for (i = 1; i <= n; i++) {
            *(s + k) = i;
            if (trienVong(k)) xepHau1(k + 1);
        }
}

int trienVong1(int k) {
    int i;
    for (i = 1; i < k; i++)
        if (*(s + k) == *(s + i)) return 0;	//moi hang chi co 1 so
    return 1;
}
//in Hoan Vi ra man hinh

int hoanVi(int k) {
    int i;
    if (k == n + 1) {
        d2++;
        printf("\n%d: ", d2);
        for (i = 1; i <= n; i++) printf("%d  ", *(s + i)); //in hoanVi 
        //printf("\n");
    } else for (i = 1; i <= n; i++) {
            *(s + k) = i;
            if (trienVong1(k)) hoanVi(k + 1); //thuchien HoanVi 
        }
}
//in Hoan vi ra file

int hoanVi1(int k) {
    int i;
    if (k == n + 1) {
        d22++;
        fprintf(f, "\n%d: ", d22);
        for (i = 1; i <= n; i++)
            fprintf(f, "%d  ", *(s + i));
        //fprintf(f, "\n");
    } else for (i = 1; i <= n; i++) {
            *(s + k) = i;
            if (trienVong1(k)) hoanVi1(k + 1);
        }
}
//to hop

void ToHop(int i) {
    int j;
    for (j = 1 + S[i - 1]; j <= n - k + i; j++) {
        *(S + i) = j;
        if (i == k) {				//neu du cau hinh thi in ra S[i]
            printf("\n%3d:", ++c);
            for (int i = 1; i <= k; i++) printf("%d ", *(S + i));
        } else ToHop(i + 1);		//goi dequy de thuc hien so tiep theo
    }
}
//chinh hop

void chinhHop(int i) {
    int j;
    for (j = 1; j <= n; j++) if (*(a + j)) {
            *(s + i) = j;
            *(a + j) = 0;				//j da dung
            if (i == k) {				//neu du cau hinh thi in ra s[i]
                printf("\n%3d:", ++c1);
                for (int i = 1; i <= k; i++) printf("%d ", *(s + i));
            } else chinhHop(i + 1);		//goi dequy de thuc hien so tiep theo
            *(a + j) = 1;				//j chua dung
        }
}
//chinh hop lap

void chinhHopLap(int i) {
    int j;
    for (j = 1; j <= n; j++) {
        *(s + i) = j;					
        if (i == k) {					//neu du cau hinh thi in ra s[i]
            printf("\n%3d:", ++c2);		//in dien dem
            for (int i = 1; i <= k; i++) printf("%d ", *(s + i));
        } else chinhHopLap(i + 1);		//goi dequy de thuc hien so tiep theo
    }
}
//in tap con cua taphop ra man hinh

void tapCon(int k) {
    int i;
    if (k == n + 1) {
        d3++;
        printf("\n%d: ", d3);
        printf("{ ");
        for (i = 1; i <= n; i++)
            if (*(s + i) == 1)
                printf("%d  ", *(a + i));
        printf("}");
    } else {
        *(s + k) = 0;
        tapCon(k + 1);
        *(s + k) = 1;
        tapCon(k + 1);
    }
}
//in tap con cua taphop ra file

void tapCom1(int k) {
    int i;
    if (k == n + 1) {
        d33++;
        fprintf(f, "\n%d: ", d33);
        fprintf(f, "{ ");
        for (i = 1; i <= n; i++)
            if (*(s + i) == 1)
                fprintf(f, "%d  ", *(a + i));
        fprintf(f, "}");
    } else {
        *(s + k) = 0;
        tapCom1(k + 1);
        *(s + k) = 1;
        tapCom1(k + 1);
    }
}
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

/*int Nhap()
{
        int i,cv1, tmp;
        FILE *fp = NULL;
        printf("De: ");
        scanf("%d",&cv1); 
        printf("\n");
        switch(cv1) 
        { 
        case 1:	
        fp = fopen("input.txt", "r");
        break;
        case 2:
        fp = fopen("input1.txt", "r");
        break;
        case 3:
        fp = fopen("input2.txt", "r");
        }
        for (i=0; i<81; i++)
    {
                fscanf(fp, "%d", &tmp);
        a1[i]= tmp;
    }
        fclose(fp);
        return 0;
}
int Xuat()
{
    int i;
    for (i=0; i<81; i++)
    {
            if ( i%9 ==0) printf("\n");
                printf(" %d", a1[i]);
    }
        printf("\n------------------");
    return 0;
}
int isOK(int i, int x1)
{
    int k, t, t1, t2;
    int kth, ktc, kto;
    int tmpX, tmpY;
    //kiem tra hang thu i da co cai nao trung chua
    t1= i%9;
    t2= i/9;
        for (k=(t2*9); k<(t2*9+9); k++)
        if (a1[k] == x1)
            return 0;
    //kiem tra cot thu j da co cai nao trung chua
    for (k=0; k<9; k++)
        if (a1[k*9+t1] == x1)
            return 0;
 
    //kiem tra trong o 3x3
    tmpX = t2%3; tmpY = t1%3;
    for (k=t2-tmpX; k<=t2-tmpX+2; k++)
        for (t=t1-tmpY; t<=t1-tmpY+2; t++)
            if (a1[k*9+t] == x1)
                return 0;
    return 1;
}
int sudoku(int i)
{
    int x1;
    while (a1[i]!=0)
        i++;
    for (x1=1; x1<=9; x1++)
        if (isOK(i, x1)) 
        {
            a1[i] = x1;
            if (i==lastK)
                Xuat();
            else
                sudoku(i+1);
            a1[i] = 0;
        }
    return 0;
}

int findLastK()
{
    int i;
    for (i=81-1; i>=0;i--)
            if (a1[i]==0)
            {
                return (i);
            }
}  
 */
int Nhap() //Lay du lieu tu file input.txt
{
    int i, tmp;
    FILE *fp = NULL;
    printf("Chon De bai 1->6 : ");
    scanf("%d", &cv1);
    switch (cv1) {							//chon de bai
        case 1:
            fp = fopen("input1.txt", "r");
            break;
        case 2:
            fp = fopen("input2.txt", "r");
            break;
        case 3:
            fp = fopen("input3.txt", "r");
            break;
        case 4:
            fp = fopen("input4.txt", "r");
            break;
        case 5:
            fp = fopen("input5.txt", "r");
            break;
        case 6:
            fp = fopen("input6.txt", "r");
    }
    fscanf(fp, "%d", &n);							
    for (i = 0; i < n * n * n * n; i++) {				//doc noi dung file
        fscanf(fp, "%d", &tmp);
        *(a1 + i) = tmp;
    }
    fclose(fp);
    return 0;
}

int Xuat() //Xuat ra man hinh
{
    int i;
    printf("----------------------------------------\n");
    for (i = 0; i < n * n * n * n; i++) {
        if (i % (n * n) == 0) printf("\n");
        printf(" %d", *(a1 + i));
    }
    printf("\n---------------------------------------");
    return 0;
}

int xuatfile() //Xuat file output.txt
{
    int i;
    FILE *fp;
    fp = fopen("KetQuaSudoku.txt", "w");
    for (i = 0; i < n * n * n * n; i++) {
        if (i == n * n * n * n) printf("\n----------------------");
        if (i % (n * n) == 0) {
            printf("\n");
            fprintf(fp, "\n");
        }
        printf(" %d", *(a1 + i));
        fprintf(fp, "%d ", *(a1 + i));
    }
    fclose(fp);
}

int isOK(int i, int x) //kiem tra hang, cot, vung
{
    int k, t, t1, t2;
    int tmpX, tmpY;
    //kiem tra hang thu i da co cai nao trung chua
    t1 = i % (n * n);
    t2 = i / (n * n);
    for (k = (t2 * n * n); k < (t2 * n * n + n * n); k++)
        if (*(a1 + k) == x)
            return 0;
    //kiem tra cot thu j da co cai nao trung chua
    for (k = 0; k < n * n; k++)
        if (a1[k * n * n + t1] == x)
            return 0;
    //kiem tra trong o nxn
    tmpX = t2 % n;
    tmpY = t1 % n;
    for (k = t2 - tmpX; k <= t2 - tmpX + n - 1; k++)
        for (t = t1 - tmpY; t <= t1 - tmpY + n - 1; t++)
            if (a1[k * n * n + t] == x)
                return 0;
    return 1;
}

int sudoku(int i) //Thu dien so vao o trong
{
    int x1;
    while (*(a1 + i) != 0)
        i++;
    for (x1 = 1; x1 <= n * n; x1++) {
        if (isOK(i, x1)) {
            *(a1 + i) = x1;
            if (i == lastK) {
                dem++;
                printf("\n----------------------------------------\n");
                printf("Cach %d la \n", dem);
                xuatfile();
                printf("\n");
            } else
                sudoku(i + 1);
            *(a1 + i) = 0;
        }
    }
    return 0;
}

int findLastK() //Tim xem con o trong hay khong
{
    int i;
    for (i = n * n * n * n - 1; i >= 0; i--)
        if (*(a1 + i) == 0)
            return i;
}

int main() {
    system("MODE CON COLS=100 LINES=59"); 							//thay doi kich thuoc khung cmd
    SetConsoleTitle("Nguyen Quoc Tan 15T2 - nqt.it.bk@gmail.com"); 	//doi ten file cmd
    printf("\n\t\t\t\tDO AN GIAI THUAT LAP TRINH C/C++ 2017");
    printf("\n\t\t\t\tNGUYEN QUOC TAN 15T2 MSSV: 102150131");
    printf("\n\t\t\t\t\tQUAY LUI & SAP XEP");

    f = fopen("array.txt", "r");
    int m = 0;
    // hoac while (feof(f) == 0)
    while (!feof(f)) {
        fscanf(f, "%d ", &a[m]);
        *(b+m)=*(a+m);
        m++;
    }
    fclose(f);
    printf("\n\nMang mo tu file array.txt la:\n");
    PrintArray(a, m);
    /*
        printf("\n\nNhap mang tu ban phim\nNhap n = ");scanf("%d",&n);
        inputArray(a,n);
        for(i=0;i<n;i++)
     		*(b+i)=*(a+i);
        printf("\n\nMang nhap tu ban phim la:\n");
        PrintArray(a,n);	*/

    printf("\n\n1.SelectSort\n");
    printf("2.InsertSort\n");
    printf("3.BubbleSort\n");
    printf("4.InterchangeSort\n");
    printf("5.ShellSort\n");
    printf("6.QuickSort\n");
    printf("7.Bai toan xep hau\n");
    printf("8.Hoan vi\n");
    printf("9.To hop\n");
    printf("10.Chinh hop k lap\n");
    printf("11.Chinh hop lap\n");
    printf("12.Tap con cua 1 taphop mo tu file\n");
    printf("13.Bai toan Ma Di Tuan\n");
    printf("14.Sudoku \n");
    printf("0.Nhan 0 de thoat\n");
    do {
        printf("\nChon Bai Toan: ");
        scanf("%d", &cv);
        printf("\n");
        switch (cv) {
            case 1:
                SelectSort(b, m);
                printf("1.Mang da sap xep Chon Truc Tiep SelectSort la :\n");
                PrintArray(b, m);
                creatFile(b, m);
                openFile(b, m);
                break;
            case 2:
                InsertSort(b, m);
                printf("2.Mang da sap xep Chen InsertSort la :\n");
                PrintArray(b, m);
                creatFile(b, m);
                openFile(b, m);
                break;
            case 3:
                BubbleSort(b, m);
                printf("3.Mang da sap xep Noi Bot BubbleSort la :\n");
                PrintArray(b, m);
                creatFile(b, m);
                openFile(b, m);
                break;
            case 4:
                InterchangeSort(b, m);
                printf("4.Mang da sap xep Doi Cho Truc tiep InterchangeSort la :\n");
                PrintArray(b, m);
                creatFile(b, m);
                openFile(b, m);
                break;
            case 5:
                ShellSort(b, m, a, m);
                printf("5.Mang da sap xep ShellSort la :\n");
                PrintArray(b, m);
                creatFile(b, m);
                openFile(b, m);
                break;
            case 6:
                QuickSort(b, 0, m - 1);
                printf("6.Mang da sap xep Nhanh la :\n");
                PrintArray(b, m);
                creatFile(b, m);
                openFile(b, m);
                break;
            case 7:
                f = fopen("xepHau.txt", "w");
                printf("7.Bai toan Xep Hau nhap tu ban phim bat ki la : ");
                printf("\nNhap n >= 4: ");
                scanf("%d", &n);
                xepHau(1);
                d1 = 0;
                xepHau1(1);
                d11 = 0;
                fclose(f);
                break;
            case 8:
                printf("8.Hoan vi cua 1 so nhap tu ban phim bat ki la : ");
                printf("\nNhap n: ");
                scanf("%d", &n);
                f = fopen("hoanVi.txt", "w");
                hoanVi(1);
                d2 = 0;
                hoanVi1(1);
                d22 = 0;
                fclose(f);
                break;
            case 9:
                printf("9.To hop cua 2 so nhap tu ban phim n>=k la : ");
                printf("\nNhap n>=k: ");
                scanf("%d%d%*c", &n, &k);
                ToHop(1);
                c = 0;
                break;
            case 10:
                printf("10.Chinh hop k lap cua 2 so nhap tu ban phim n>=k la : ");
                printf("\nNhap n>=k: ");
                scanf("%d%d%*c", &n, &k);
                for (int j = 1; j <= n; j++) *(a + j) = 1;
                chinhHop(1);
                c1 = 0;
                break;
            case 11:
                printf("11.Chinh hop lap cua 2 so nhap tu ban phim bat ki la : ");
                printf("\nNhap n, k bat ki : ");
                scanf("%d%d%*c", &n, &k);
                chinhHopLap(1);
                c2 = 0;
                break;
            case 12:
                printf("12.Tap con cua mang mo tu file array1.txt la : ");
                f = fopen("array1.txt", "r");
                n = 0;
                // hoac while (feof(f) == 0)
                while (!feof(f)) {
                    n++;
                    fscanf(f, "%d ", &a[n]);
                }
                f = fopen("tapCon.txt", "w");
                tapCon(1);
                d3 = 0;
                tapCom1(1);
                d33 = 0;
                fclose(f);
                break;
            case 13:
                printf("13.Bai toan Ma Di Tuan(Ban co 5x5 -> 8x8)");
                f = fopen("MaDiTuan.txt", "w");
                nhapdl();
                khoitao();
                MaDiTuan(x1, y1, 1);
                printf("--------------------------------------------------------");
                printf("\nVay co tong cong %d cach de con ma di het ban co!(^_^)\n", sc);
                fprintf(f, "--------------------------------------------------------");
                fprintf(f, "\nVay co tong cong %d cach de con ma di het ban co!(^_^)", sc);
                fclose(f);
                break;
            case 14:
                Nhap();
                lastK = findLastK();
                printf("De bai %d:\n",cv1);
                Xuat();
                printf("\nGiai de %d\n",cv1);
                sudoku(0);
                printf("\nVay tong cong co %d cach giai Sudoku nay (^_^)\n", dem);
                dem = 0;
        }
    } while (cv != 0);
    return 0;
}

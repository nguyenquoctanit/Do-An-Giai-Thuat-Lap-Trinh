#include <iostream>
#include <winbgim.h>
#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <ctime>
using namespace std ;

int a[121],mx[121],my[121];
int n = 81,cv1;
int color=4;
int sdk=0;
int last;
 
int Nhap();
int Xuat();
int xuatfile();
int Try(int i);
int isOK(int i, int x);
int findlast();
 
int main()
{
	initwindow(550,550);
	setwindowtitle("Giai Sodoku");
	setbkcolor(LIGHTGREEN) ;
	cleardevice() ;
	setcolor(BLACK) ;
	settextstyle (3,VERT_DIR,2);
	outtextxy(350,40,"PRESS ANY KEY");
	int x=50,y=50;
	for (x=50; x<=450; x+=50)
	for (y=50; y<=450; y+=50)
	rectangle(x,y,x+50,y+50);
    Nhap();
    last = findlast();
    int i;
    int x1=80,y1=90;
    for (i=0; i<=81; i++)
    {
    	char *s;
		itoa(a[i],s,10);
		if(x1==80+50*9) { x1=80;y1+=50;};
		if (a[i]!=0){
		outtextxy(x1,y1,s);
		mx[i]=0;
		my[i]=0;
		}
		else{
			mx[i]=x1;
			my[i]=y1;
		}
		x1+=50;
    }
    getch();
    xuatfile();
    Try(0);
    if(sdk) outtextxy(350,40,"SUCCESSFUL !!!"); else outtextxy(350,40,"DATA ERROR  !!!");
    getch();
    return 0;
}
 
int Nhap() //lay du lieu tu file input.txt
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
}
    
    for (i=0; i<81; i++)
    {
            fscanf(fp, "%d", &tmp);
            a[i]= tmp;
    }
    fclose(fp);
    return 0;
}
 
int Xuat() //xuat ra man hinh
{
    int i;
    for (i=0; i<81; i++)
    {
	    if ( i%9 ==0) printf("\n");
		printf(" %d", a[i]);
        
    }
    return 0;
}

int xuatfile() //Xuat file output.txt
{
	int i;
	FILE *fp;
    fp=fopen("output.txt","w"); 
    for (i=0; i<81; i++)
    {
	    if ( i == 81) printf("\n----------------------");
	    	if(i%(9)==0)
				{	
					printf("\n");
					fprintf(fp,"\n");
					}
			printf(" %d", a[i]);
			fprintf(fp,"%d ", a[i]);
    }
    fclose(fp);	
} 

int Try(int i) //Dien so bat ky vao cac o trong, o nao da co so thi bo qua
{
    int x;
    while (a[i]!=0)
        i++;
    for (x=1; x<=9; x++)
        if (isOK(i, x)) 
        {
            a[i] = x;
            if (i==last){
            	sdk=1;
                setcolor(color);
                color+=1;
                if(color==6) color=4;
			    for(int d=0;d<81;d++)
			    {
			    	char *s = new char[2];
			    	s[1]=0;
			    	if((mx[d]!=0)&&(my[d]!=0)) {
			    		s[0]=a[d]+0x30;
			    		outtextxy(mx[d],my[d],s);
			    		}
			    }
			    getch();
                }
            else
                Try(i+1);
            a[i] = 0;
        }
    return 0;
}
 
int isOK(int i, int x) //Kiem tra hang, cot va vung
{
    int k, t, t1, t2;
    int kth, ktc, kto;
    int tmpX, tmpY;
    //kiem tra hang thu i da co cai nao trung chua
    t1= i%9;
    t2= i/9;
	for (k=(t2*9); k<(t2*9+9); k++)
        if (a[k] == x)
            return 0;
    //kiem tra cot thu j da co cai nao trung chua
    for (k=0; k<9; k++)
        if (a[k*9+t1] == x)
            return 0;
 
    //kiem tra trong o 3x3
    tmpX = t2%3; tmpY = t1%3;
    for (k=t2-tmpX; k<=t2-tmpX+2; k++)
        for (t=t1-tmpY; t<=t1-tmpY+2; t++)
            if (a[k*9+t] == x)
                return 0;
    return 1;
}
 
int findlast() //Kiem tra xem con o trong nao khong?
{
    int i;
    for (i=81-1; i>=0;i--)
            if (a[i]==0)
            {
                return (i);
            }
}  


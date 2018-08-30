#include <bits/stdc++.h>



int main(){
    int cases;
    scanf("%d",&cases);
    for(int i = 0; i < cases; i++){
        int px,py,qx,qy;
    	scanf("%d %d %d %d",&px,&py,&qx,&qy);
    	int rx = 2 * qx - px;
		int ry = 2 * qy - py;
		printf("%d %d\n",rx,ry);
	}


    return 0;
}

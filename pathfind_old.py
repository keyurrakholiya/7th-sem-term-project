
import numpy as np
import setting
import time
import com


row = 8
col = 8
loop_no= row * col   ##(it should be 20*20 = 400 idealy)


path = np.arange(400).reshape(4,100)
map1 = np.arange(loop_no).reshape(row,col)
#map1 =[1,1,1,1,1,1,1,1,1,1,1,1],[1,2,0,0,0,0,0,0,0,1,0,1],[1,0,0,1,0,1,1,0,0,1,0,1],[1,0,0,1,1,1,1,0,0,1,0,1],[1,0,1,0,0,1,1,0,0,1,0,1],[1,1,1,1,0,0,0,0,1,1,1,1],[1,1,1,1,0,0,0,0,0,1,1,1],[1,0,0,0,0,1,1,0,0,1,0,1],[1,0,0,1,0,1,1,0,0,1,0,1],[1,0,0,1,1,1,1,0,0,1,0,1],[1,0,0,0,'R',1,1,0,0,1,0,1],[1,1,1,1,1,1,1,1,1,1,1,1]

map1=[1,1,1,1,1,1,1,1],[1,0,0,'R',0,0,0,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1],[1,2,0,0,0,0,0,1],[1,1,1,1,1,1,1,1]


'''
[1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,'R',1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,1],
[1,2,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1]



[1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,0,0,0,0,0,0,0,1,0,1],
[1,0,0,1,0,1,1,0,0,1,0,1],
[1,0,0,1,1,1,1,0,0,1,0,1],
[1,0,1,0,0,1,1,0,0,1,0,1],
[1,1,1,1,0,0,0,0,1,1,1,1],
[1,1,1,1,0,0,0,0,0,1,1,1],
[1,0,0,0,0,1,1,0,0,1,0,1],
[1,0,0,1,0,1,1,0,0,1,0,1],
[1,0,0,1,1,1,1,0,0,1,0,1],
[1,0,0,0,'R',1,1,0,0,1,0,1],
[1,1,1,1,0,0,1,0,1,1,1,1]

'''

cordinate = 0





changed_r_row4 = 0
changed_r_col4 = 0

changed_r_row1 = 0
changed_r_col1 = 0

changed_r_row2 = 0
changed_r_col2 = 0

changed_r_row3 = 0
changed_r_col3 = 0



changed_left_r_row1 = 0
changed_left_r_col1 = 0

changed_left_r_row2 = 0
changed_left_r_col2 = 0

changed_left_r_row3 = 0
changed_left_r_col3 = 0

changed_left_r_row4 = 0
changed_left_r_col4 = 0

setting.ind1=0
setting.ind2=0
setting.ind3=0
setting.ind4=0;
I=0
J=0

def flush():

    i=0;
    j=0;
    k=0;
    I=0;
    J=0;
    l=0;
    setting.temp1=0;
    setting.temp2=0;
    setting.temp3=0;
    setting.temp4=0;
    setting.sum1=0;
    setting.sum2=0;
    setting.sum3=0;
    setting.sum4=0;
    setting.temp  = 2;
    r1=0;
    r2=0;
    r3=0;
    r4=0;
    c1=0;
    c2=0;c3=0;
    c4=0;
    setting.flag = 1;
    length=0;
    setting.path_num = 0
    setting.r_row = 0
    setting.r_col = 0




def path_find():
    global row
    global col
    global loop_no
    flush();
    for k in range(0,4):
        for l in range(0,100):
            path[k][l] = 0;
            setting.ind1 = 0;
            setting.ind2 = 0;
            setting.ind3 = 0;
            setting.ind4 = 0;

    for i in range(0,row):
        for j in range(0,col):
            if(map1[i][j] == 2): ##fsetting.ind goal 'G'
                map1[i][j] = 2;
                setting.row_desti = i;
                setting.col_desti = j;
    #print "destination location" ,setting.row_desti, setting.col_desti
        
    while(setting.temp < loop_no):
        ##printf("\n value of setting.temp = %d" ,setting.temp);
        for i in range(0,row):
            for j in range(0,col):
                #print i,j,'A'
                if(map1[i][j] == setting.temp):				##printf("\n value of k = %d" ,k);
                    if((map1[i][j+1] != 1) & (map1[i][j+1] != 'R') & (map1[i][j+1] < 2)):
                        map1[i][j+1] = setting.temp + 1;
                    if((map1[i][j-1] != 1) & (map1[i][j-1] != 'R') & (map1[i][j-1] < 2)):
                        map1[i][j-1] = setting.temp + 1;
                    if((map1[i+1][j] != 1) & (map1[i+1][j] != 'R') & (map1[i+1][j] < 2)):
                        map1[i+1][j] = setting.temp + 1;
                    if((map1[i-1][j] != 1) & (map1[i-1][j] != 'R') & (map1[i-1][j] < 2)):
                        map1[i-1][j] = setting.temp + 1;
        setting.temp = setting.temp + 1;
        
    
#fsetting.ind out location of robot
    for I in range(0,row):
        for J in range(0,col):
            if(map1[I][J] == 'R'): 
                i = I
                setting.r_row = I
                j = J
                setting.r_col = J
    #print "robot location", i,j


    setting.temp1 = map1[i][j-1]; 
    r1 = i;
    c1 = j-1;    ##column decrement 
    path[0][setting.ind1] = r1;
    path[0][setting.ind1+1] = c1;
    setting.sum1 = setting.temp1;
        
        
    setting.temp2 = map1[i][j+1]; ##columne increment
    r2 = i;
    c2 = j+1;
    path[1][setting.ind2] = r2;
    path[1][setting.ind2+1] = c2;
    setting.sum2 = setting.temp2;
        ##printf("setting.temp2= %d",setting.sum2);

    setting.temp3 = map1[i+1][j]; ##row increment
    r3 = i+1;
    c3 = j;
    path[2][setting.ind3] = r3;
    path[2][setting.ind3+1] = c3;
    setting.sum3 = setting.temp3;
        ##printf("setting.temp3= %d",setting.sum3);

    setting.temp4 = map1[i-1][j]; ##row decrement
    r4 = i-1;
    c4 = j;
    path[3][setting.ind4] = r4;
    path[3][setting.ind4+1] = c4;   
    setting.sum4 = setting.temp4;


    while(setting.flag == 1):
                
        if(setting.temp1 > 2):
            
            if(map1[r1][c1-1] == map1[r1][c1] - 1):
                setting.sum1 = setting.sum1 + map1[r1][c1-1];
                setting.temp1 = map1[r1][c1-1];
                    
                setting.ind1= setting.ind1 + 2;
                path[0][setting.ind1]= r1;
                path[0][setting.ind1+1] = c1-1;
                                
                if(map1[r1][c1-1] == 2):
                    setting.flag = 0;
                c1 = c1 - 1;
                                        
            elif(map1[r1][c1+1] == map1[r1][c1] - 1):
            
                setting.sum1 = setting.sum1 + map1[r1][c1+1];
                setting.temp1 = map1[r1][c1+1];
                    
                setting.ind1= setting.ind1 + 2;
                path[0][setting.ind1]= r1;
                path[0][setting.ind1+1] = c1+1;
                    
                if(map1[r1][c1+1] == 2):
                    setting.flag = 0;
                c1 = c1 + 1;
                
            elif(map1[r1+1][c1] == map1[r1][c1] - 1):
                setting.sum1 = setting.sum1 + map1[r1+1][c1];
                setting.temp1 = map1[r1+1][c1];

                setting.ind1 = setting.ind1 + 2;
                path[0][setting.ind1]= r1+1;
                path[0][setting.ind1+1] = c1;

                if(map1[r1+1][c1] == 2):
                    setting.flag = 0;
                r1 = r1 +1;
                    
            elif(map1[r1-1][c1] == map1[r1][c1] -1 ):
                setting.sum1 = setting.sum1 + map1[r1-1][c1];
                setting.temp1 = map1[r1-1][c1];

                setting.ind1 = setting.ind1 + 2;
                path[0][setting.ind1]= r1-1;
                path[0][setting.ind1+1] = c1;                   

                if(map1[r1-1][c1] == 2):
                    setting.flag = 0;
                r1 = r1 -1;
                
                        

        if(setting.temp2 > 2 ):
            #print r2,c2,"B"
            if(map1[r2][c2+1] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2][c2+1];
                setting.temp2 = map1[r2][c2+1];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2;
                path[1][setting.ind2+1] = c2+1;

                if(map1[r2][c2+1] == 2):
                    setting.flag = 0;
                c2 = c2 + 1;

                
                
            elif(map1[r2][c2-1] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2][c2-1];
                setting.temp2 = map1[r2][c2-1];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2;
                path[1][setting.ind2+1] = c2-1;

                if(map1[r2][c2-1] == 2):
                    setting.flag = 0;
                c2 = c2 - 1;

            elif(map1[r2+1][c2] == map1[r2][c2] - 1):
                setting.sum2 = setting.sum2 + map1[r2+1][c2];
                setting.temp2 = map1[r2+1][c2];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2 +1;
                path[1][setting.ind2+1] = c2;

                if(map1[r2+1][c2] ==2 ):
                    setting.flag = 0;     
                r2 = r2 + 1;
                    
            elif(map1[r2-1][c2] == map1[r2][c2] -1 ):
                setting.sum2 = setting.sum2 + map1[r2-1][c2];
                setting.temp2 = map1[r2-1][c2];

                setting.ind2 = setting.ind2 + 2;
                path[1][setting.ind2]= r2-1;
                path[1][setting.ind2+1] = c2;

                if(map1[r2-1][c2] == 2):
                    setting.flag = 0;
                r2 = r2 - 1;
                
            
        
        
        if(setting.temp3 > 2 ):	##row increment
        
            if(map1[r3][c3+1] == map1[r3][c3] - 1):
                setting.sum3 = setting.sum3 + map1[r3][c3+1];
                setting.temp3 = map1[r3][c3+1];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3;
                path[2][setting.ind3+1] = c3+1;
                if(map1[r3][c3+1] == 2):
                    setting.flag = 0;
                c3 = c3 + 1;
                
            elif(map1[r3+1][c3] == map1[r3][c3] - 1):
                setting.sum3 = setting.sum3 + map1[r3+1][c3];
                setting.temp3 = map1[r3+1][c3];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3+1;
                path[2][setting.ind3+1] = c3;
                        
                if(map1[r3+1][c3] == 2):
                    setting.flag = 0;
                r3 = r3 + 1;
                
            elif(map1[r3-1][c3] == map1[r3][c3] - 1):
                
                    
                setting.sum3 = setting.sum3 + map1[r3-1][c3];
                setting.temp3 = map1[r3-1][c3];
                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3-1;
                path[2][setting.ind3+1] = c3;
                if(map1[r3-1][c3] == 2):
                    setting.flag = 0;
                r3 = r3 - 1;
                
            elif(map1[r3][c3-1] == map1[r3][c3] -1 ):
                setting.sum3 = setting.sum3 + map1[r3][c3-1];
                setting.temp3 = map1[r3][c3-1];

                setting.ind3 = setting.ind3 + 2;
                path[2][setting.ind3]= r3;
                path[2][setting.ind3+1] = c3-1;
            
                if(map1[r3][c3-1] == 2):
                    setting.flag = 0;
                c3 = c3 -1;
                
                                
        if(setting.temp4 > 2 ):  ##row decrem
            if(map1[r4][c4+1] == map1[r4][c4] - 1): 
                setting.sum4 = setting.sum4 + map1[r4][c4+1];
                setting.temp4 = map1[r4][c4+1];

                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4;
                path[3][setting.ind4+1] = c4+1;

                if(map1[r4][c4+1] == 2):
                    setting.flag = 0;
                c4 = c4 + 1;

                
                
            elif(map1[r4-1][c4] == map1[r4][c4] - 1):
                setting.sum4 = setting.sum4 + map1[r4-1][c4];
                setting.temp4 = map1[r4-1][c4];
                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4-1;
                path[3][setting.ind4+1] = c4;

                if(map1[r4-1][c4] == 2):
                    setting.flag = 0;
                r4 = r4 - 1;
                
            elif(map1[r4+1][c4] == map1[r4][c4] - 1):
                setting.sum4 = setting.sum4 + map1[r4+1][c4];
                setting.temp4 = map1[r4+1][c4];

                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4+1;
                path[3][setting.ind4+1] = c4;

                if(map1[r4+1][c4] == 2):
                    setting.flag = 0;
                r4 = r4 + 1;
                
            elif(map1[r4][c4-1] == map1[r4][c4] -1 ):
                setting.sum4= setting.sum4 + map1[r4][c4-1];
                setting.temp4 = map1[r4][c4-1];
                setting.ind4 = setting.ind4 + 2;
                path[3][setting.ind4]= r4;
                path[3][setting.ind4+1] = c4-1;
                    
                if(map1[r4][c4-1] == 2):
                    setting.flag = 0;
                c4 = c4 - 1;

    path_set = 0                           
    for k in range(0,4):
        for l in range(0,99):
            if((path[k][l] == setting.row_desti) & (path[k][l+1] == setting.col_desti) & (path_set == 0)):
                print("final path number is %d ",k);
                setting.path_num = k;
                path_set = 1
        l = l+ 2;
        print path[k]
############################################################################################


            
    
            
                

def main():
    path_find();
    while (setting.go):
        for i in range(0,row):
            print map1[i]
        if(path[setting.path_num][cordinate] == setting.r_row + 1):
            ##no need to change head setting.position
            if(setting.pos == 0):
                print("forward \n");
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find();
            
            elif(setting.pos == 90):
                print("right forward \n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find()
                   
            elif(setting.pos == 270):
                print("left forward \n");
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                com.brake()
                com.left()
                com.forward()
                
                setting.pos = 0;
                path_find();
            
            elif(setting.pos == 180):
                print("180 forward ");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row + 1][setting.r_col] = 'R';
                setting.pos = 0;
                path_find();

        elif((path[setting.path_num][cordinate]) == setting.r_row - 1):
        
            ##change head 180 upside
            

            if(setting.pos == 90):
                print("left forward \n");
                com.brake()
                com.left()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();

            elif(setting.pos == 270):
                print("right forward \n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();
                
            
            elif(setting.pos == 180):
                print("forward \n");
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0
                map1[setting.r_row - 1][setting.r_col] = 'R';
            
                setting.pos = 180;
                path_find();

            elif(setting.pos == 0):
            
                print("180 forward keyurrrrrrrrrrrrrrrrr\n");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row][setting.r_col]  = 0;
                map1[setting.r_row - 1][setting.r_col] = 'R';
                setting.pos = 180;
                path_find();
            
        

        elif(path[setting.path_num][cordinate+1] ==  setting.r_col + 1):  ##left   
            if(setting.pos == 0):
                print("left forward\n");
                com.brake()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
                
            elif(setting.pos == 90):
                print("forward \n");
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
            
            elif(setting.pos == 180):
                print("right forward\n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();
                
            elif(setting.pos == 270):
                print("180 forward\n");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col + 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 90;
                path_find();

        elif(path[setting.path_num][cordinate+1] ==  setting.r_col - 1):          
            if(setting.pos == 0):
                print("right forward\n");
                com.brake()
                com.right()
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();
                
            elif(setting.pos == 270 ):
                print("forward\n");
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();
            
            elif(setting.pos == 180):
                print("left forward\n");
                com.brake()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();    
            
            elif(setting.pos == 90):
                print("180 forward\n");
                com.brake()
                com.left()
                com.left()
                com.forward()
                
                map1[setting.r_row ][setting.r_col - 1] = 'R';
                map1[setting.r_row][setting.r_col]  = 0
                setting.pos = 270;
                path_find();

                        
                                
        if((path[setting.path_num][cordinate+2]== setting.row_desti) & (path[setting.path_num][cordinate+3] == setting.col_desti)): 
                if(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 0)):
                        print("\t left forward");
                        com.brake()
                        com.left()
                        com.forward()
                        
                        map1[setting.r_row][setting.r_col+1] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 90
                        setting.go = 0;
                        
                elif(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 180)):
                        print("\tright  forward");
                        com.brake()
                        com.right()
                        com.forward()
                        
                        map1[setting.r_row][setting.r_col+1] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos =90
                        setting.go = 0;
                        
                elif(((setting.r_col + 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 90)):
                        print("1time forward");
                        com.forward()
                        map1[setting.r_row][setting.r_col+1] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 90
                        
                        
                        
                                
                        
                        ##col decre
                elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 0)):
                        print("\tright  forward");
                        com.brake()
                        com.right()
                        com.forward()
                        
                        map1[setting.r_row][setting.r_col - 1] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 270
                        setting.go = 0; 
                        
                elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 180)):
                        print("\tleft  forward");
                        com.brake()
                        com.left()
                        com.forward()
                
                        map1[setting.r_row][setting.r_col - 1] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 270
                        setting.go = 0; 
                                        
                elif(((setting.r_col - 1) == path[setting.path_num][cordinate+1] )&( setting.pos == 270)):
                        print("1time forward");
                        com.forward()
                        map1[setting.r_row][setting.r_col - 1] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 270
                        
                                
                        ##row incre
                elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 270)):
                        print("\tleft  forward");
                        com.brake()
                        com.left()
                        com.forward()
                        
                        map1[setting.r_row + 1][setting.r_col] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 0
                        setting.go = 0; 
                                
                elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 90)):
                        print("\tright  forward");
                        com.brake()
                        com.right()
                        com.forward()
                        
                        map1[setting.r_row + 1][setting.r_col] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.go = 0;
                        setting.pos = 0
                                
                elif(((setting.r_row + 1) == path[setting.path_num][cordinate] )&( setting.pos == 0)):
                        print(" forward");
                        com.forward()
                        map1[setting.r_row + 1][setting.r_col] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 0
                       
                        
                        ##row decre
                elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos == 90)):
                        print("\tleft forward");
                        com.brake()
                        com.left()
                        com.forward()
                        
                        map1[setting.r_row - 1][setting.r_col] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 180
                        setting.go = 0; 
                        
                elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos ==270)):
                        print("\tright  forward");
                        com.brake()
                        com.right()
                        com.forward()
                        
                        setting.go = 0;
                        map1[setting.r_row - 1][setting.r_col] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos =180
                                
                elif(((setting.r_row - 1) == path[setting.path_num][cordinate] )&( setting.pos == 180)):
                        print("\t1 forward");
                        com.forward()
                        map1[setting.r_row - 1][setting.r_col] = 'R'
                        map1[setting.r_row][setting.r_col]  = 0
                        setting.pos = 180
                setting.go = 0
                print "done"
                break;

            
       # check_obs()
        path_find()
       # time.sleep(1)

setting.init()


def important_fun():
     
    for I in range(0,row):
        for J in range(0,col):
            if(map1[I][J] == 'R'): 
                i = I
                setting.r_row = I
                j = J
                setting.r_col = J

    for i in range(0,row):
        print map1[i]
                
    print "robot location", i,j
    print setting.pos
    if(setting.pos == 0):
        if((setting.r_row + 1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
           print "forward stop"
           com.forward()
           com.brake()

        elif((setting.r_row == setting.row_desti) & (setting.r_col + 1 == setting.col_desti)):
           print "left forward stop"
           com.brake()
           com.left()
           com.forward()
           com.brake()

        elif((setting.r_row == setting.row_desti) & (setting.r_col -1 == setting.col_desti)):
           print "rihgt forward stop"
           com.brake()
           com.right()
           com.forward()
           com.brake()
           
    if(setting.pos == 90):
        if((setting.r_row + 1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
            print "right forward stop"
            com.brake()
            com.right()
            com.forward()
            com.brake()
           
        elif((setting.r_row == setting.row_desti) & (setting.r_col + 1 == setting.col_desti)):
            print "forward stop"
            com.forward()
            com.brake()
            
        elif((setting.r_row - 1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
             print "left forwawrd stop"
             com.brake()
             com.left()
             com.forward()
             com.brake()
           
    if(setting.pos == 180):
        if((setting.r_row - 1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
           print "forward stop"
           com.forward()
           com.brake()
            

        elif((setting.r_row == setting.row_desti) & (setting.r_col + 1 == setting.col_desti)):
           print "right forward stop"
           com.brake()
           com.right()
           com.forward()
           com.brake()

        elif((setting.r_row == setting.row_desti) & (setting.r_col -1 == setting.col_desti)):
           print "left forward stop"
           com.brake()
           com.left()
           com.forward()
           com.brake()
           
    if(setting.pos == 270):
        if((setting.r_row + 1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
            print "left forward stop"
            com.brake()
            com.left()
            com.forward()
            com.brake()
           
        elif((setting.r_row == setting.row_desti) & (setting.r_col - 1 == setting.col_desti)):
            print "forward stop"
            com.forward()
            com.brake()
            
           
        elif((setting.r_row - 1 == setting.row_desti) & (setting.r_col == setting.col_desti)):
             print "right forwawrd stop"
             com.brake()
             com.right()
             com.forward()
             com.brake()
           
main()
important_fun()


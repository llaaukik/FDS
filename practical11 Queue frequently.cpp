#include <iostream>
using namespace std;
#include<stdio.h> //Standard Input Output Header

#define SIZE 5
void enqueue(int x); //add element to rear(end)
void dequeue(); //remove element at front        (void)return type
void display();
int FRONT=-1;
int REAR=-1;
int QUEUE[SIZE];
int main()
{
    int x,ch;
      while(1){
        cout<<"\n1:Add Job";
        cout<<"\n2:Delete Job";
        cout<<"\n3:Display";
        cout<<"n4:Exit Your Choice:";
        cin>>ch;
        {  
            case1:
            cout<<"Enter Job:";
            cin>>x;
            enqueue(x);
            break;
            case2:
            dequeue();
            break;
            case3:
            display();
            break;
            case4:
              exit(0);
}
      }

} void enqueue(int x)
{
    if (REAR>=SIZE-1)
    cout<<"Queue is overflow";
    else{
        REAR=REAR+1;
        QUEUE[REAR]=x;
        if (FRONT==-1)
        FRONT=0;
    }
}void dequeue(){
    if(FRONT==-1)
    cout<<"Queue is overflow";
    else{
        cout<<"Deleted element is:"<<QUEUE[FRONT];
        if(FRONT==REAR){
            FRONT=-1;
            REAR=-1;
        }else
        {
            FRONT=FRONT+1;
        }
    }
}void display()
{
    int i;
    if (FRONT==-1)
    cout<<"Queueis empty\n";
    else{
        for(i=FRONT;i<=REAR;i++)
        cout<<"QUEUE[i]";
    }
}


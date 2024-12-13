
#include<iostream>
using namespace std;

struct node
{
    int prn;
    string name;
    struct node *next;
};

class linklist
{
    node *president,*secretory;
    public:
    linklist()
    {
        president = NULL;
        secretory =NULL;

    }
    void addMembers();
    void countMember();
    void deleteMember();
    void display();
    void displayReverse();
    void concatList();
    void deletePresident();



};

void linklist::addMembers()
{
    node *newmember = new node();
    cout<<"Enter the PRN of student";
    cin>>newmember->prn;
    cout<<"Enter name of Student:";
    cin>>newmember->name;
    
    if(president == NULL)
    {
        president = newmember;
        secretory = newmember;
    }
    else{
        secretory->next=newmember;
        secretory=newmember;
    }
}

void linklist::countMember()
{
    node*temp = president;
    int count =0;
    if(president == NULL)
    {
        cout<<"List is empty & count is :"<<count;

    }
    else
    {
        while(temp!=NULL)
        {
            count++;
            temp = temp->next;
        }
        cout<<" \n Total no of Members : "<< count;
    }
}

void linklist::deletePresident()
{
    int no;
    node*temp;
     
    temp = president;
    president=president->next;
    delete(temp);

}

void linklist::deleteMember()
{
    int no;
    node*temp;
    node*temp1;
    int f=0;
    cout<<"Enter the prn no of student : ";
    cin>>no;
    if(president == NULL)
    {
        cout <<"List is empty";
    }
    else{
        temp = president;
        
        while (temp!=NULL)
        {
            if(temp->prn==no)
            {
               temp1->next=temp->next;
                delete(temp);
                f=1;
            }
            temp1 = temp;
            temp = temp->next;
        
            
        }
        if(f==0)
        {
            cout<<"Member mot found";
        }
        
         
        
    }
   
}

void linklist:: display()
{
    node * temp;
    temp= president;
    if(president == NULL)
    {
        cout<<"LIst is empty";
    }
    else{
        while (temp!=NULL)
        {
            cout<<" \n PRN : "<<temp->prn;
            cout<<"\n Name :" <<temp->name;
            temp = temp->next;
            
        }
        
    }

    
}
void linklist::concatList()
{ 
    int k,j,i;
    node*president1,*president2,*temp1,*temp2;
    cout<<"enter no. of members in list1: ";
    cin>>k;
    president=NULL;
    for(i=0;i<k;i++)
    {
        addMembers();
        president1=president;
    }
    president=NULL;
    cout<<"enter no. of members in list2: ";
    cin>>j;
    for(i=0;i<j;i++)
    {
        addMembers();
        president2=president;
    }
    president=NULL;
    temp1=president1;
    while(temp1->next!=NULL)
    {
         temp1=temp1->next;
    }
    temp1->next=president2;

    temp2=president1;

    while(temp2!=NULL)
    {
        cout<<"\n "<<temp2->prn<<" "<<temp2->name<<"\n";
        temp2=temp2->next;
    }

}

void linklist::displayReverse()
{
    node *curr,*temp ;
    node*beforeNode =NULL;
    node*afterNode = NULL;
    curr = president;
   while(curr!=NULL)
    {
        afterNode = curr->next;
        curr->next = beforeNode;
        beforeNode = curr;
        curr = afterNode;
    }
    president = beforeNode;
    temp = president;
    while (temp != NULL) {
            cout << temp->prn << " ";
            cout<< temp->name << " ";
            temp = temp->next;
        }
}

int main()
{
    linklist a;
    int i;
    char ch;
    do{
        cout<<"\n 1. To add Members ";
        cout<<"\n 2. To count member ";
        cout<<"\n 3. To delete presedent.";
        cout<<"\n 4. To delete member ";
        cout<<"\n 5. To display members ";         
        cout<<"\n 6. To display list in reverse order ";
        cout<<"\n 7.To concatenate two list ";
        cout<<"\n Enter the choice: ";
        cin>>i;
        switch(i)
        {
            case 1: a.addMembers();
            break;
            case 2: a.countMember();
            break;
            case 3: a.deletePresident();
            break;
            case 4: a.deleteMember();
            break;
            
            case 5: a.display();
            break;
            case 6: a.displayReverse();
            break;
            case 7: a.concatList();
            break;
           
            default: cout<<"\n unknown choice";
      }
        cout<<"\n do you want to continue enter y/Y: ";
        cin>>ch;
    }while(ch=='y'||ch=='Y');
    return 0;
}


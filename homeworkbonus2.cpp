
#include<bits/stdc++.h>
struct Student{
	int Score ;
	char Name[30];
};
using namespace std;
struct Student s[10];

void Maxstudent(){
	int i ,m=0,n=0;
	for(i=0;i<10;i++){
		if(s[i].Score > m ){
			m = s[i].Score;
			n=i;
		}
		
	
	}
	cout << "Max Score: "<< m << " Name Student: " <<s[n].Name << endl;
}

void Minstudent(){
	int i ,m=100, n=0;
	for(i=0;i<10;i++){
		if( m > s[i].Score){
			m = s[i].Score;
			n=i;
		}

	
	}
	cout << "Max Score: "<< m << " Name Student: " <<s[n].Name <<endl;
}

float AverScore(int stds){
	int i=0;
	float sum=0;
	for (i;i<stds;i++){
		sum+=s[i].Score;
	}
	return sum/10;
}

void ModeScore(){
	int check[101] = {}, Mode = 0, SM;
    for(int i = 0; i < 10; i++)
    {
        check[s[i].Score]++;
        if(check[s[i].Score] > Mode)
        {
            Mode = check[s[i].Score];
            SM = s[i].Score;
        }
    }
    cout<< "ModeScore: " << SM << endl;
}

void MedianScore(){
 char namee[30];
    int point;
    float med;
    for(int i=0;i<10;i++){
        int min = 100;
        int minn = 0;
        for(int j=i;j<10;j++){
            if (s[j].Score <= min){
                min = s[j].Score;
                minn = j;
            }
        }
        strcpy(namee,s[i].Name);
        point = s[i].Score;
        strcpy(s[i].Name,s[minn].Name);
        s[i].Score = s[minn].Score;
        strcpy(s[minn].Name,namee);
        s[minn].Score = point;
    }
    cout<<"MedianScore : "<< (s[4].Score+s[5].Score)/2 << endl;
}


float SDScore(int stds){
	float summ = 0;
    float mean,standardDeviation,sd;
    for(int i=0;i<stds;i++){
        summ += s[i].Score;
    }
    mean = summ/stds;
    for(int j=0;j<stds;j++) {
    standardDeviation += pow(s[j].Score - mean, 2);
  }
   return sqrt(standardDeviation / stds);
	
}

void Show(int stds){
	int avr=AverScore(stds), SD=SDScore(stds), i;
	for(i=0;i<stds;i++){
		if(s[i].Score> avr+2*SD){
			cout << s[i].Name <<" Gread : A" <<endl; 
		}
		else if (s[i].Score > avr+SD ){
			cout << s[i].Name <<" Gread : B" <<endl; 
		}
		else if (s[i].Score > avr ){
			cout << s[i].Name <<" Gread : C" <<endl; 
		}
		else if (s[i].Score > avr-SD ){
			cout << s[i].Name <<" Gread : D" <<endl; 
		}
		else{
			cout << s[i].Name <<" Gread : F" <<endl; 
		}
	}
	
	
}
using namespace std;
int main(){
	int stds = 10;
	
	s[0].Score = 98;
	strcpy(s[0].Name,"Ploy");
	s[1].Score = 54;
	strcpy(s[1].Name,"Jane");
	s[2].Score = 74;
	strcpy(s[2].Name,"Opal");
	s[3].Score = 51;
	strcpy(s[3].Name,"Ohm");
	s[4].Score = 66;
	strcpy(s[4].Name,"Pond");
	s[5].Score = 40;
	strcpy(s[5].Name,"Bond");
	s[6].Score = 50;
	strcpy(s[6].Name,"Grab");
	s[7].Score = 54;
	strcpy(s[7].Name,"Jame");
	s[8].Score = 51;
	strcpy(s[8].Name,"Pong");
	s[9].Score = 49;
	strcpy(s[9].Name,"Kar");
	

	Maxstudent();
	Minstudent();
	cout << "AverScore: " << AverScore(stds)<<endl;
	ModeScore();
	MedianScore();
	cout<<"SD score : "<< SDScore(stds)<<endl;
	Show(stds);
}
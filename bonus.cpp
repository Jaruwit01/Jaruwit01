#include<iostream>
#include <string>
#include<bits/stdc++.h>
#include <algorithm> 
struct Studens{
	int Score ;
	char Name[30];
};
using namespace std;
struct Studens s[10];

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

void AverScore(){
	int i=0,sum=0;
	for (i;i<10;i++){
		sum+=s[i].Score;
	}
	cout << "AverScor : " << sum/10;
}

//int ModeScore(){
//	
//}
//
//int MedianScore(){
//	
//}
//
//int SdScore(){
//	
//}

using namespace std;
int main(){
	int stds = 10;
	
	s[0].Score = 98;
	strcpy(s[0].Name,"Ploy");
	s[1].Score = 84;
	strcpy(s[1].Name,"Jane");
	s[2].Score = 74;
	strcpy(s[2].Name,"Opal");
	s[3].Score = 99;
	strcpy(s[3].Name,"Ohm");
	s[4].Score = 82;
	strcpy(s[4].Name,"Pond");
	s[5].Score = 97;
	strcpy(s[5].Name,"Bornd");
	s[6].Score = 55;
	strcpy(s[6].Name,"Grab");
	s[7].Score = 88;
	strcpy(s[7].Name,"Jame");
	s[8].Score = 64;
	strcpy(s[8].Name,"Rew");
	s[9].Score = 49;
	strcpy(s[9].Name,"Kar");
	
//	for(int i=0; i<stds;i++){
//		cout << s[i].Name << endl;
//		
//	}
	Maxstudent();
	Minstudent();
	AverScore();
}

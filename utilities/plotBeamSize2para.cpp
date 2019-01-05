#include <iostream>
#include <fstream>

void plotBeamSize2para() {
  
  int label;
  double sigma_probability;
  double temp[19] = {};
  double sigma_value[] = {0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0};

  // read file
  ifstream ifs("/home/accel/work/dnn/saves/cnn/2para/prediction_sigmay.csv");

  // canvas
  TCanvas* cvs = new TCanvas("cvs", "cvs", 1200, 900);
  gStyle->SetTitleOffset(1.5, "y");
  cvs->Divide(4,3);

  // histgram
  int bins = 100;
  float ent_min = -0.4;
  float ent_max = 0.4;
  
  // 0.2
  TH1D* h1 = new TH1D("h1", "correct_val : 0.2 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[0]+ent_min, sigma_value[0]+ent_max);
  // 0.4
  TH1D* h2 = new TH1D("h2", "correct_val : 0.4 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[1]+ent_min, sigma_value[1]+ent_max);
  // 0.6
  TH1D* h3 = new TH1D("h3", "correct_val : 0.6 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[2]+ent_min, sigma_value[2]+ent_max);
  // 0.8
  TH1D* h4 = new TH1D("h4", "correct_val : 0.8 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[3]+ent_min, sigma_value[3]+ent_max);
  // 1.0
  TH1D* h5 = new TH1D("h5", "correct_val : 1.0 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[4]+ent_min, sigma_value[4]+ent_max);
  // 1.2
  TH1D* h6 = new TH1D("h6", "correct_val : 1.2 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[5]+ent_min, sigma_value[5]+ent_max);
  // 1.4
  TH1D* h7 = new TH1D("h7", "correct_val : 1.4 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[6]+ent_min, sigma_value[6]+ent_max);
  // 1.6
  TH1D* h8 = new TH1D("h8", "correct_val : 1.6 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[7]+ent_min, sigma_value[7]+ent_max);
  // 1.8
  TH1D* h9 = new TH1D("h9", "correct_val : 1.8 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[8]+ent_min, sigma_value[8]+ent_max);
  // 2.0
  TH1D* h10 = new TH1D("h10", "correct_val : 2.0 #sigma_{x};#sigma_{x};Entries ", bins, sigma_value[9]+ent_min, sigma_value[9]+ent_max);

  char ch; //comma
  while( ifs >> label >> ch >> temp[0] >> ch >> temp[1] >> ch >> temp[2] >> ch >> temp[3] >> ch >> temp[4] >> ch >> temp[5] >> ch >> temp[6] >> ch >> temp[7] >> ch >> temp[8] >> ch >> temp[9] ) {

    double sigma_probability = 0;
    for( int i = 0; i < 10; i++ ) {
      sigma_probability += sigma_value[i] * temp[i];
    }

    if( label == 0 ) {
      h1->Fill( sigma_probability );
    }
    else if( label == 1 ) {
      h2->Fill( sigma_probability );
    }
    else if( label == 2 ) {
      h3->Fill( sigma_probability );
    }
    else if( label == 3 ) {
      h4->Fill( sigma_probability );
    }
    else if( label == 4 ) {
      h5->Fill( sigma_probability );
    }
    else if( label == 5 ) {
      h6->Fill( sigma_probability );
    }
    else if( label == 6 ) {
      h7->Fill( sigma_probability );
    }
    else if( label == 7 ) {
      h8->Fill( sigma_probability );
    }
    else if( label == 8 ) {
      h9->Fill( sigma_probability );
    }
    else if( label == 9 ) {
      h10->Fill( sigma_probability );
    }
  }

  // output
  cvs->cd(1);
  h1->Draw();

  cvs->cd(2);
  h2->Draw();

  cvs->cd(3);
  h3->Draw();

  cvs->cd(4);
  h4->Draw();

  cvs->cd(5);
  h5->Draw();

  cvs->cd(6);
  h6->Draw();

  cvs->cd(7);
  h7->Draw();

  cvs->cd(8);
  h8->Draw();

  cvs->cd(9);
  h9->Draw();

  cvs->cd(10);
  h10->Draw();
}

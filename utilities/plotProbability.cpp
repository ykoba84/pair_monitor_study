#include <iostream>
#include <fstream>

void plotProbability() {
  
  int label;
  int weight[19] = {};
  double sigma_probability[19][19] = {};
  double temp[19] = {};
  double sigma_value[] = {0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8};

  // read file
  ifstream ifs("/home/accel/work/dnn/saves/cnn/miniVGG/prediction.csv");

  // canvas
  TCanvas* cvs = new TCanvas("cvs", "cvs", 1200, 900);
  gStyle->SetTitleOffset(1.5, "y");
  cvs->Divide(4,3);

  const TString labels[] = {"0.0", "0.2", "0.4", "0.6", "0.8", "1.0", "1.2", "1.4", "1.6", "1.8", "2.0", "2.2", "2.4", "2.6", "2.8", "3.0", "3.2", "3.4", "3.6", "3.8"};
  // histgram
  double xmin = 0;
  double xmax = 4;
  int bins = 20;
  int ent_min = -1;
  int ent_max = 1;
  
  // 1.0
  TH1D* h1 = new TH1D("h1", "correct_val : 1.0 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 1.2
  TH1D* h2 = new TH1D("h2", "correct_val : 1.2 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 1.4
  TH1D* h3 = new TH1D("h3", "correct_val : 1.4 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 1.6
  TH1D* h4 = new TH1D("h4", "correct_val : 1.6 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 1.8
  TH1D* h5 = new TH1D("h5", "correct_val : 1.8 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 2.0
  TH1D* h6 = new TH1D("h6", "correct_val : 2.0 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 2.2
  TH1D* h7 = new TH1D("h7", "correct_val : 2.2 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 2.4
  TH1D* h8 = new TH1D("h8", "correct_val : 2.4 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 2.6
  TH1D* h9 = new TH1D("h9", "correct_val : 2.6 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 2.8
  TH1D* h10 = new TH1D("h10", "correct_val : 2.8 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);
  // 3.0
  TH1D* h11 = new TH1D("h11", "correct_val : 3.0 #sigma_{y};#sigma_{y};Probability ", bins, xmin, xmax);

  char ch; //comma
  while( ifs >> label >> ch >> temp[0] >> ch >> temp[1] >> ch >> temp[2] >> ch >> temp[3] >> ch
	 >> temp[4] >> ch >> temp[5] >> ch >> temp[6] >> ch >> temp[7] >> ch >> temp[8] >> ch
	 >> temp[9] >> ch >> temp[10] >> ch >> temp[11] >> ch >> temp[12] >> ch >> temp[13] >> ch
	 >> temp[14] >> ch >> temp[15] >> ch >> temp[16] >> ch >> temp[17] >> ch >> temp[18] ) {

    for( int i = 0; i < 19; i++ ) {
      sigma_probability[label][i] += temp[i];
    }

    weight[label]++;
  }

  for( int i = 0; i < 19; i++ ) {

    for( int j = 0; j < 19; j++ ) {

      if( i == 4 )		h1->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 5 )		h2->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 6 )		h3->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 7 )		h4->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 8 )		h5->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 9 )		h6->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 10 )	h7->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 11 )	h8->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 12 )	h9->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 13 )	h10->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
      else if( i == 14 )	h11->Fill(sigma_value[j], sigma_probability[i][j]/weight[i]);
    }
  }

  h1->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h1->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h1->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h1->GetYaxis()->SetRangeUser(0,1);

  h2->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h2->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h2->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h2->GetYaxis()->SetRangeUser(0,1);

  h3->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h3->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h3->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h3->GetYaxis()->SetRangeUser(0,1);

  h4->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h4->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h4->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h4->GetYaxis()->SetRangeUser(0,1);

  h5->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h5->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h5->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h5->GetYaxis()->SetRangeUser(0,1);

  h6->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h6->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h6->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h6->GetYaxis()->SetRangeUser(0,1);

  h7->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h7->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h7->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h7->GetYaxis()->SetRangeUser(0,1);

  h8->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h8->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h8->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h8->GetYaxis()->SetRangeUser(0,1);

  h9->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h9->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h9->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h9->GetYaxis()->SetRangeUser(0,1);

  h10->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h10->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h10->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h10->GetYaxis()->SetRangeUser(0,1);

  h11->GetXaxis()->SetNdivisions(20, 1, 1, false);
  h11->GetXaxis()->SetLabelSize(0.05);
  for( int i = 0; i < 20; i++ ) {
    h11->GetXaxis()->SetBinLabel(i+1, labels[i]);
  }
  h11->GetYaxis()->SetRangeUser(0,1);

  cvs->cd(1);
  h1->Draw("HIST");

  cvs->cd(2);
  h2->Draw("HIST");

  cvs->cd(3);
  h3->Draw("HIST");

  cvs->cd(4);
  h4->Draw("HIST");

  cvs->cd(5);
  h5->Draw("HIST");

  cvs->cd(6);
  h6->Draw("HIST");

  cvs->cd(7);
  h7->Draw("HIST");

  cvs->cd(8);
  h8->Draw("HIST");

  cvs->cd(9);
  h9->Draw("HIST");

  cvs->cd(10);
  h10->Draw("HIST");

  cvs->cd(11);
  h11->Draw("HIST");
  
}

#include <iostream>
#include <fstream>

void plotBeamSize2paraGraph1() {
  
  int label;
  double sigma_probability;
  double temp[19] = {};
  double sigma_value[] = {0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0};

  // read file
  ifstream ifs("/home/accel/work/dnn/saves/cnn/2para_zenbu/prediction_sigmay.csv");

  // canvas
  TCanvas* cvs = new TCanvas("cvs", "cvs", 1200, 900);
  gStyle->SetTitleOffset(1.1, "y");
  gStyle->SetTitleSize(0.05, "xy");
  gStyle->SetLabelSize(0.05, "xy");
  
  // legend
  TLegend* leg = new TLegend(0.15, 0.35, 0.45, 0.85);
  
  // histgram
  int bins = 100;
  float ent_min = -0.4;
  float ent_max = 0.4;
  
  TH1D* h1 = new TH1D("h1", "", 500, 0.2, 2.0);
  h1->SetStats(0);
  h1->SetLineColor(kRed+3);
  h1->SetFillStyle(3001);
  h1->SetFillColor(kRed+2);
  TH1D* h2 = (TH1D*)h1->Clone();
  h2->SetLineColor(kOrange+3);
  h2->SetFillStyle(3001);
  h2->SetFillColor(kOrange+2);
  TH1D* h3 = (TH1D*)h1->Clone();
  h3->SetLineColor(kYellow+2);
  h3->SetFillStyle(3001);
  h3->SetFillColor(kYellow+1);
  TH1D* h4 = (TH1D*)h1->Clone();
  h4->SetLineColor(kSpring+4);
  h4->SetFillStyle(3001);
  h4->SetFillColor(kSpring+3);
  TH1D* h5 = (TH1D*)h1->Clone();
  h5->SetLineColor(kGreen+4);
  h5->SetFillStyle(3001);
  h5->SetFillColor(kGreen+3);
  TH1D* h6 = (TH1D*)h1->Clone();
  h6->SetLineColor(kTeal+3);
  h6->SetFillStyle(3001);
  h6->SetFillColor(kTeal+2);
  TH1D* h7 = (TH1D*)h1->Clone();
  h7->SetLineColor(kCyan+3);
  h7->SetFillStyle(3001);
  h7->SetFillColor(kCyan+2);
  TH1D* h8 = (TH1D*)h1->Clone();
  h8->SetLineColor(kAzure+3);
  h8->SetFillStyle(3001);
  h8->SetFillColor(kAzure+2);
  TH1D* h9 = (TH1D*)h1->Clone();
  h9->SetLineColor(kBlue+3);
  h9->SetFillStyle(3001);
  h9->SetFillColor(kBlue+2);
  TH1D* h10 = (TH1D*)h1->Clone();
  h10->SetLineColor(kViolet+3);
  h10->SetFillStyle(3001);
  h10->SetFillColor(kViolet+2);
  /*
  TH1D* h11 = (TH1D*)h1->Clone();
  h11->SetLineColor(kMagenta+3);
  h11->SetFillStyle(3001);
  h11->SetFillColor(kMagenta+2);
  */

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

  // okesyo
  h1->GetYaxis()->SetRangeUser(0, 2000);

  h1->Draw();
  h2->Draw("same");
  h3->Draw("same");
  h4->Draw("same");
  h5->Draw("same");
  h6->Draw("same");
  h7->Draw("same");
  h8->Draw("same");
  h9->Draw("same");
  h10->Draw("same");
  
    // legend
  leg->AddEntry(h1, "#sigma_{y} = 0.2 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h2, "#sigma_{y} = 0.4 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h3, "#sigma_{y} = 0.6 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h4, "#sigma_{y} = 0.8 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h5, "#sigma_{y} = 1.0 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h6, "#sigma_{y} = 1.2 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h7, "#sigma_{y} = 1.4 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h8, "#sigma_{y} = 1.6 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h9, "#sigma_{y} = 1.8 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h10, "#sigma_{y} = 2.0 #sigma_{y}^{TDR}", "lf");

  leg->Draw();
}

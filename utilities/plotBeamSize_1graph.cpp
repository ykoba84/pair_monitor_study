#include <iostream>
#include <fstream>

void plotBeamSize_1graph() {
  
  int label;
  double sigma_probability;
  double temp[19] = {};
  double sigma_value[] = {0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8};

  // read file
  ifstream ifs("/home/accel/work/dnn/saves/cnn/miniVGG/prediction.csv");

  // canvas
  TCanvas* cvs = new TCanvas("cvs", "cvs", 800, 600);
  gStyle->SetTitleOffset(1.1, "y");
  gStyle->SetTitleSize(0.04, "xy");
  gStyle->SetLabelSize(0.05, "xy");
  //cvs->Divide(4,3);

  // legend
  TLegend* leg = new TLegend(0.6, 0.3, 0.88, 0.88);

  // histgram
  int bins = 100;
  int ent_min = -1;
  int ent_max = 1;

  // 1.0
  TH1D* h1 = new TH1D("h1", ";#sigma_{y}/#sigma_{y}^{TDR};", 500, 0.0, 4.0);
  h1->SetStats(0);
  h1->SetLineColor(kRed+3);
  h1->SetFillStyle(3001);
  h1->SetFillColor(kRed+2);
  TH1D* h0 = (TH1D*)h1->Clone();
  h0->SetLineColor(kPink+4);
  h0->SetFillStyle(3001);
  h0->SetFillColor(kPink+2);  
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
  TH1D* h11 = (TH1D*)h1->Clone();
  h11->SetLineColor(kMagenta+3);
  h11->SetFillStyle(3001);
  h11->SetFillColor(kMagenta+2);

  char ch; //comma
  while( ifs >> label >> ch >> temp[0] >> ch >> temp[1] >> ch >> temp[2] >> ch >> temp[3] >> ch >> temp[4] >> ch >> temp[5] >> ch >> temp[6] >> ch >> temp[7] >> ch >> temp[8] >> ch >> temp[9] >> ch >> temp[10] >> ch >> temp[11] >> ch >> temp[12] >> ch >> temp[13] >> ch >> temp[14] >> ch >> temp[15] >> ch >> temp[16] >> ch >> temp[17] >> ch >> temp[18] ) {

    double sigma_probability = 0;
    for( int i = 0; i < 19; i++ ) {
      sigma_probability += sigma_value[i] * temp[i];
    }

    if( label == 3 ) {
        h0->Fill( sigma_probability );
    }
    else if( label == 4 ) {
      h1->Fill( sigma_probability );
    }
    else if( label == 5 ) {
      h2->Fill( sigma_probability );
    }
    else if( label == 6 ) {
      h3->Fill( sigma_probability );
    }
    else if( label == 7 ) {
      h4->Fill( sigma_probability );
    }
    else if( label == 8 ) {
      h5->Fill( sigma_probability );
    }
    else if( label == 9 ) {
      h6->Fill( sigma_probability );
    }
    else if( label == 10 ) {
      h7->Fill( sigma_probability );
    }
    else if( label == 11 ) {
      h8->Fill( sigma_probability );
    }
    else if( label == 12 ) {
      h9->Fill( sigma_probability );
    }
    else if( label == 13 ) {
      h10->Fill( sigma_probability );
    }
    else if( label == 14 ) {
      h11->Fill( sigma_probability );
    }
  }

  h0->Scale();
  h1->Scale(h0->GetEntries() / h1->GetEntries());
  h2->Scale(h0->GetEntries() / h2->GetEntries());
  h3->Scale(h0->GetEntries() / h3->GetEntries());
  h4->Scale(h0->GetEntries() / h4->GetEntries());
  h5->Scale(h0->GetEntries() / h5->GetEntries());
  h6->Scale(h0->GetEntries() / h6->GetEntries());
  h7->Scale(h0->GetEntries() / h7->GetEntries());
  h8->Scale(h0->GetEntries() / h8->GetEntries());
  h9->Scale(h0->GetEntries() / h9->GetEntries());
  h10->Scale(h0->GetEntries() / h10->GetEntries());
  h11->Scale(h0->GetEntries() / h11->GetEntries());

  h0->Draw("hist");
  h1->Draw("same hist");
  h2->Draw("same hist");
  h3->Draw("same hist");
  h4->Draw("same hist");
  h5->Draw("same hist");
  h6->Draw("same hist");
  h7->Draw("same hist");
  h8->Draw("same hist");
  h9->Draw("same hist");
  h10->Draw("same hist");
  h11->Draw("same hist");

  // legend
  leg->AddEntry(h0, "#sigma_{y} = 0.8 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h1, "#sigma_{y} = 1.0 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h2, "#sigma_{y} = 1.2 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h3, "#sigma_{y} = 1.4 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h4, "#sigma_{y} = 1.6 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h5, "#sigma_{y} = 1.8 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h6, "#sigma_{y} = 2.0 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h7, "#sigma_{y} = 2.2 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h8, "#sigma_{y} = 2.4 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h9, "#sigma_{y} = 2.6 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h10, "#sigma_{y} = 2.8 #sigma_{y}^{TDR}", "lf");
  leg->AddEntry(h11, "#sigma_{y} = 3.0 #sigma_{y}^{TDR}", "lf");

  //leg->Draw();
  
  /*
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

  cvs->cd(11);
  h11->Draw();
  */
}

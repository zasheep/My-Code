//***********************************************************************************
// Julia set by complex iteration
//
// Given complex value c and escape radius R (satisfying R(R-1)>=|c|) the (quadratic) Julia set J(c) is
// formed by the set of all Complex numbers for which
//
// J(c) = { z : for all n, z_{n+1}=(z_n)^2+c satisfies |z_{n+1}|<=R with initial value z_0=z}
//
// If z is not in J(c) then there will be some Whole number k with |z_k|>R (satarting z_0=z).
// This value can be used to determine a colour for the Complex number z in the Complex plane, all
// z in J(c) being coloured black (RGB=000).
//***************************************************************************
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import java.io.*;
import javax.imageio.*;
import javax.swing.*;
import java.util.*;
public class Julia
  {
  private static Scanner input = new Scanner(System.in);
  public static void main(String[] args) throws IOException
    {
    int ht = 15000;
    int wd = 15000;
    double R=0.0;  // Escape region
    System.out.println("Real c value: (for z_{n+1} = (z_n)^2+c)");
    double rec = input.nextDouble();
    System.out.println("Im c value: (for z_{n+1} = (z_n)^2+c)");
    double imc = input.nextDouble();
    double csize = Math.sqrt(rec*rec+imc*imc);
    //R = 0.5+Math.sqrt(1.0+4.0*csize)/2.0;
    System.out.println("Escape radius R (should satisfy R(R-1)>=|c|):");
    R = input.nextDouble();
    while ((R*(R-1.0)<csize))
      {
      System.out.println("Escape radius R (should satisfy R(R-1)>=|c|):");
      R = input.nextDouble();
      };
    double re_low = -(R+0.5);
    double re_high = (R+0.5);
    double im_low = -(R+0.5);
    double im_high = (R+0.5);
    double rez;
    if (R<2)
      {
      re_low = (-2.0);
      re_high = 3.5;
      im_low = (-2.5);
      im_high = 2.5;
      };

    double imz;
    double trez;
    double timz;
    double xnew;
    double ynew;
    int drop_out = 150;   // if |z_n|<=R for all n<=150 assume z is in J(c)
    int tests_made;
    double re_inc = (re_high-re_low)/((double)wd);
    double im_inc = (im_high-im_low)/((double)ht);
    int xc;
    int yc;
    //int colours = 178;
    //int colours = 255;
    int colours = 1024;
    int[] seen = new int[drop_out+1];
    int[][] colouring = new int[wd][ht];
    int[] palette = new int[colours];
    boolean inside;
    File CompImage = new File("JuliaSet+Re"+rec+"Im"+imc+".jpg");
    BufferedImage img2 = new BufferedImage(wd,ht, BufferedImage.TYPE_INT_RGB );
    // Set (default) colour palette
    // Complex values assigned colour depending on exit time: resident (ie in J(c)) coloured Black;
    palette[0]=(255);
    for (int clr=1; clr<colours; clr++)
      {
      // To experiment with different colour templates, modify the 3 lines below:
      // (value)<<16 is the RED component in RGB
      // (value)<<8  is the GREEN
      // (value)     is the BLUE
      // Different functions of the index can be used, but is necessary to ensure component value is 8 bits, hence
      // modulo 256 operation
      int REDQ = ((clr)*(clr)*(clr))%256;  // How much Red
      int GREENQ = ((clr)*(clr)*(clr))%256;  // How much Green
      int BLUEQ =(clr*clr)%256;  // How much Blue
      palette[clr] = (REDQ<<16)|(GREENQ<<8)|(BLUEQ);
      };
    for (int ctr=0; ctr<drop_out+1; ctr++)
      {
      seen[ctr]=0; 
      };
    //************************************************************
    // Main process: iterate z_{n+1} = z_n^2+(rc,ic)
    // Classify (x,y) in Complex plane by how long to exit
    //************************************************************
    for (xc=0; xc<wd; xc++)
      {
      for (yc=0; yc<ht; yc++)
        {
        // Next z moving through Complex Plane
        rez = re_low+(double)(xc)*re_inc;
        imz = im_low+(double)(yc)*im_inc;
        tests_made=0;
        // Initiate z_0
        rez=rez+rec; imz=imz+imc;
        inside = (((rez*rez+imz*imz)<R*R));
        // Iterate z_{n+1}=(z_n)^2+c until either escape radius exceeded or z in J(c)
        while ((tests_made<drop_out)&&(inside))  
          {
          xnew = rez*rez-imz*imz+rec;
          ynew = 2*rez*imz+imc;
          rez = xnew ; imz=ynew;
          inside = (((rez*rez+imz*imz)<R*R));
          tests_made++;
          };
          colouring[xc][yc]=tests_made;
          seen[tests_made]++;
        };
       };
        // Now map from palette colours to escape times 
        int next_col=0;
        for (int map=0; map<drop_out+1; map++)
          {
          if (seen[map]>0)
            {
            seen[map]=next_col; next_col=(next_col+1)%(colours);
            };
          };
          // Finally generate Image
          for (xc=0; xc<wd; xc++)
            {
            for (yc=0; yc<ht; yc++)
              {
              if (colouring[xc][yc]>=drop_out)
                {
                img2.setRGB(xc, ht-1-yc, 0); // Inside Julia set: colour BLACK
                }
             else
               {
               int coll = colouring[xc][yc];
               img2.setRGB(xc,ht-1-yc,palette[seen[coll]]); // Outside set: colour gradated on number needed
               };
            };
          };

   ImageIO.write(img2, "JPG", CompImage);
};
}
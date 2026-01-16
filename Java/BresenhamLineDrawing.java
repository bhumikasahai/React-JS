import java.util.*;
public class BresenhamLineDrawing{
    public static void bresenham(int x1, int y1, int x2, int y2 ){
        int dx = x2-x1;
        int dy = y2-y1;
        int d = 2*dy-dx;
        int dE = 2*dy;
        int dNE = 2*(dy-dx);
        while(x1!=x2){
            System.out.println("("+x1+","+y1+")");
            if(d<=0){
                d += dE;
                x1++;
            }else{
                d += dNE;
                x1++;
                y1++;
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter x1 y1 x2 y2 (space separated):");
        try {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            bresenham(x1, y1, x2, y2);
        } catch (Exception e) {
            System.out.println("Invalid input! Please enter four integers.");
        }
        sc.close();
    }
}
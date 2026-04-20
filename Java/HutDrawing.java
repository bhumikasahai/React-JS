import java.awt.*;
import javax.swing.*;

public class HutDrawing extends JPanel {

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;


        setBackground(Color.CYAN);

        
        g.setColor(new Color(139, 69, 19));  
        g.fillRect(100, 200, 200, 150);      

        g.setColor(new Color(160, 82, 45));   
        g.fillRect(170, 270, 60, 80);        

        g.setColor(Color.DARK_GRAY);        
        int[] xRoof = {90, 200, 310};
        int[] yRoof = {200, 120, 200};
        g.fillPolygon(xRoof, yRoof, 3);      

        g.setColor(new Color(105, 105, 105)); 
        g.fillRect(240, 130, 20, 50);

        // Optional: add windows
        g.setColor(Color.WHITE);
        g.fillRect(120, 220, 30, 30);        
        g.fillRect(250, 220, 30, 30);        
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Hut Drawing in Java");
        HutDrawing hut = new HutDrawing();
        frame.add(hut);
        frame.setSize(450, 450);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

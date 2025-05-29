import javax.swing.*;
import java.awt.*;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;

public class ShearTransformation extends JPanel {

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        // Original rectangle
        Rectangle2D rect = new Rectangle2D.Double(50, 50, 100, 60);
        g2d.setColor(Color.BLUE);
        g2d.draw(rect);

        // Apply shear transformation
        AffineTransform shear = new AffineTransform();
        shear.shear(0.5, 0.0); // Shear along X-axis (0.5 is the shear factor)

        Shape shearedRect = shear.createTransformedShape(rect);
        g2d.setColor(Color.RED);
        g2d.draw(shearedRect);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Shear Transformation Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.add(new ShearTransformation());
        frame.setVisible(true);
    }
}
import java.io.PrintWriter;

@javax.servlet.annotation.WebServlet(name = "Course")

public class Course extends javax.servlet.http.HttpServlet {
    protected void doPost(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, java.io.IOException {
    }

    protected void doGet(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, java.io.IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Hello World!</title>");
        out.println("</head>");
        out.println("<bdoy>");
        out.println("<h1>hello</h1>");
        out.println("</body>");
        out.println("</html>");
        out.flush();
        out.close();
    }
}

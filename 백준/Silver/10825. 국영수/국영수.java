import java.util.*;
import java.io.*;

class Student {
    String name;
    int kor, eng, math;

    // 생성자
    Student(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Student> students = new ArrayList<>();
        StringTokenizer st;

        // 입력 받기
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int kor = Integer.parseInt(st.nextToken());
            int eng = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());

            students.add(new Student(name, kor, eng, math));
        }

        // 정렬 수행
        students.sort((s1, s2) -> {
            if (s1.kor != s2.kor) return s2.kor - s1.kor;  // 국어 내림차순
            if (s1.eng != s2.eng) return s1.eng - s2.eng;  // 영어 오름차순
            if (s1.math != s2.math) return s2.math - s1.math;  // 수학 내림차순
            return s1.name.compareTo(s2.name);  // 이름 오름차순 (사전순)
        });

        // 출력 최적화
        StringBuilder sb = new StringBuilder();
        for (Student s : students) {
            sb.append(s.name).append("\n");
        }
        System.out.println(sb);
    }
}
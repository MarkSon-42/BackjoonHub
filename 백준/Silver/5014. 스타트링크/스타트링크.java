import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int F = sc.nextInt();
        int S = sc.nextInt();
        int G = sc.nextInt();
        int U = sc.nextInt();
        int D = sc.nextInt();
        
        int[] visited = new int[F + 1];
        Arrays.fill(visited, -1);  // 방문 여부와 버튼 누른 횟수를 저장하는 배열 선언 및 초기화
        Queue<Integer> q = new LinkedList<>();  // 큐 선언하고,

        q.add(S);  // 시작점을 큐에 삽입
        visited[S] = 0;

        while (!q.isEmpty()) {
            int current = q.poll();

            if (current == G) {
                System.out.println(visited[current]);
                return;
            }

            // 위로 올라갈 수 있고, 올라갈 곳이 방문하지 않는 곳인지 체크
            if (current + U <= F && visited[current + U] == -1) {
                visited[current + U] = visited[current] + 1;  // 방문과 동시에 버튼 횟수 증가 반영
                q.add(current + U);  // 위로 이동한 층을 큐에 삽입
            }

            if (current - D >= 1 && visited[current - D] == -1) {  // 내려갈 수 있으며, 방문하지 않았는지 체크
                visited[current - D] = visited[current] + 1;
                q.add(current - D);
            }
        }
        System.out.println("use the stairs");
    }
}
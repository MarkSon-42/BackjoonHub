import java.util.Stack;

class Solution {
    boolean solution(String s) {  // String type 매개변수 s를 받음
        Stack<Character> stack = new Stack<>();  // Character 타입의 요소를 저장할 수 있는 새로운 stack 객체 생성. '(' 저장할 용도로 사용
        
        for (char c : s.toCharArray()) { // 입력 문자열 s를 문자 배열로 반환하고, 각 문자에 대해 반복. c는 현재 처리중인 문자를 나타냄
            if (c == '(') {
                stack.push(c);
            }
            else if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }  
}
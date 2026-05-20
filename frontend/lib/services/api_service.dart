import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static Future<Map<String, dynamic>> analyze(String content) async {
    final response = await http.post(
      Uri.parse('http://127.0.0.1:8000/analyze'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'content': content,
      }),
    );

    return jsonDecode(response.body);
  }
}
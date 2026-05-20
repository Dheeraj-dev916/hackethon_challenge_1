import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static Future<Map<String, dynamic>> analyze(String content) async {
    final response = await http
        .post(
      Uri.parse('http://127.0.0.1:8000/analyze'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'content': content,
      }),
    )
        .timeout(
      const Duration(seconds: 120),
      onTimeout: () {
        throw Exception('API request timed out after 120 seconds');
      },
    );

    if (response.statusCode != 200) {
      throw Exception(
        'API error (${response.statusCode}): ${response.body}',
      );
    }

    try {
      return jsonDecode(response.body) as Map<String, dynamic>;
    } catch (e) {
      throw Exception('Failed to parse API response: $e');
    }
  }
}

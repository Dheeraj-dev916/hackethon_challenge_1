import 'dart:convert';
import 'package:flutter/flutter.dart';
import '../services/api_service.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  final TextEditingController controller = TextEditingController();

  bool isLoading = false;
  Map<String, dynamic>? result;
  String? errorMessage;

  // Safe nested getter for handling missing keys
  dynamic _safeGet(Map<String, dynamic>? map, List<String> keys) {
    dynamic current = map;
    for (final key in keys) {
      if (current is Map<String, dynamic>) {
        current = current[key];
      } else {
        return 'N/A';
      }
    }
    return current ?? 'N/A';
  }

  Future<void> runWorkflow() async {
    if (controller.text.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please enter some content to analyze'),
        ),
      );
      return;
    }

    setState(() {
      isLoading = true;
      errorMessage = null;
    });

    try {
      final response = await ApiService.analyze(controller.text);

      setState(() {
        result = response;
      });
    } catch (e) {
      setState(() {
        errorMessage = 'Error: $e';
      });
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(errorMessage!),
          duration: const Duration(seconds: 5),
        ),
      );
    } finally {
      setState(() {
        isLoading = false;
      });
    }
  }

  Widget sectionCard({
    required String title,
    required String content,
    required Color borderColor,
    required IconData icon,
  }) {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(bottom: 20),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: const Color(0xFF111111),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(
          color: borderColor,
          width: 2,
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                icon,
                color: borderColor,
                size: 30,
              ),
              const SizedBox(width: 10),
              Text(
                title,
                style: TextStyle(
                  color: borderColor,
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 20),
          Text(
            content,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 18,
              height: 1.6,
            ),
          ),
        ],
      ),
    );
  }

  Widget stateBox({
    required String title,
    required String content,
    required Color color,
  }) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(20),
        decoration: BoxDecoration(
          color: color.withOpacity(0.15),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: color,
            width: 2,
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              title,
              style: TextStyle(
                color: color,
                fontSize: 26,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            Expanded(
              child: SingleChildScrollView(
                child: Text(
                  content,
                  style: TextStyle(
                    color: color.withOpacity(0.9),
                    fontSize: 20,
                    height: 1.5,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: const Color(0xFF1A1A1A),
        elevation: 0,
        centerTitle: true,
        title: const Text(
          '🧠 Antigravity Action Agent',
          style: TextStyle(
            color: Color(0xFF00F0FF),
            fontWeight: FontWeight.bold,
            fontSize: 34,
          ),
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: const Color(0xFF1A1A1A),
                borderRadius: BorderRadius.circular(25),
                border: Border.all(
                  color: Colors.white54,
                  width: 2,
                ),
              ),
              child: TextField(
                controller: controller,
                maxLines: 8,
                enabled: !isLoading,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                ),
                decoration: const InputDecoration(
                  border: InputBorder.none,
                  hintText: 'Paste business report / news / dashboard data...',
                  hintStyle: TextStyle(
                    color: Colors.grey,
                    fontSize: 18,
                  ),
                ),
              ),
            ),
            const SizedBox(height: 30),
            SizedBox(
              width: double.infinity,
              height: 70,
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF00D9FF),
                  foregroundColor: Colors.black,
                  disabledBackgroundColor: Colors.grey,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(40),
                  ),
                ),
                onPressed: isLoading ? null : runWorkflow,
                child: isLoading
                    ? const CircularProgressIndicator(
                        color: Colors.black,
                      )
                    : const Text(
                        'Orchestrate Agent Workflow',
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
              ),
            ),
            const SizedBox(height: 35),
            if (errorMessage != null)
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.red.withOpacity(0.2),
                  borderRadius: BorderRadius.circular(15),
                  border: Border.all(color: Colors.red, width: 2),
                ),
                child: Text(
                  errorMessage!,
                  style: const TextStyle(
                    color: Colors.redAccent,
                    fontSize: 16,
                  ),
                ),
              ),
            if (result != null) ...[
              sectionCard(
                title: 'Deep Insights',
                content: _safeGet(result, [
                  'antigravity_execution',
                  'results',
                  'InsightAgent',
                  'primary_insight',
                ]).toString(),
                borderColor: const Color(0xFF00F0FF),
                icon: Icons.search,
              ),
              sectionCard(
                title: 'Real-World Impact',
                content: _safeGet(result, [
                  'antigravity_execution',
                  'results',
                  'ImpactAgent',
                  'business_impact',
                ]).toString(),
                borderColor: Colors.orange,
                icon: Icons.warning_amber_rounded,
              ),
              sectionCard(
                title: 'System Action',
                content: _safeGet(result, [
                  'antigravity_execution',
                  'results',
                  'DecisionAgent',
                  'recommended_action',
                ]).toString(),
                borderColor: Colors.greenAccent,
                icon: Icons.flash_on,
              ),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.black,
                  border: Border.all(
                    color: Colors.white54,
                    width: 2,
                  ),
                ),
                child: SingleChildScrollView(
                  child: Text(
                    _buildExecutionLogs(),
                    style: const TextStyle(
                      color: Color(0xFF5DFFB3),
                      fontSize: 20,
                      height: 1.7,
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 30),
              Row(
                children: [
                  stateBox(
                    title: 'BEFORE',
                    content: _safeGet(result, [
                      'antigravity_execution',
                      'results',
                      'SimulationAgent',
                      'system_state_before',
                    ]).toString(),
                    color: Colors.redAccent,
                  ),
                  const SizedBox(width: 20),
                  stateBox(
                    title: 'AFTER',
                    content: _safeGet(result, [
                      'antigravity_execution',
                      'results',
                      'SimulationAgent',
                      'system_state_after',
                    ]).toString(),
                    color: Colors.greenAccent,
                  ),
                ],
              ),
              const SizedBox(height: 40),
              const Text(
                '⚙️ Antigravity Agent Trace (Workplan, Tasks, Reasoning Flow)',
                style: TextStyle(
                  color: Color(0xFF00F0FF),
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 15),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: const Color(0xFF0A0A0A),
                  borderRadius: BorderRadius.circular(15),
                  border: Border.all(color: const Color(0xFF333333), width: 2),
                ),
                child: SelectableText(
                  _buildTraceJson(),
                  style: const TextStyle(
                    color: Colors.greenAccent,
                    fontSize: 14,
                    fontFamily: 'monospace',
                    height: 1.5,
                  ),
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }

  String _buildExecutionLogs() {
    final logs = _safeGet(result, [
      'antigravity_execution',
      'results',
      'SimulationAgent',
      'execution_logs',
    ]);

    if (logs is List) {
      return logs.join('\n');
    } else if (logs is String) {
      return logs;
    } else {
      return logs.toString();
    }
  }

  String _buildTraceJson() {
    try {
      final workplan = _safeGet(result, ['antigravity_workflow_plan']) ?? 'N/A';
      final trace = _safeGet(result, [
            'antigravity_execution',
            'workflow_trace',
          ]) ??
          'N/A';

      return const JsonEncoder.withIndent('  ').convert({
        '1. Workplan & Tasks': workplan,
        '2. Decision Flow & Trace': trace,
      });
    } catch (e) {
      return 'Error rendering trace: $e';
    }
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }
}

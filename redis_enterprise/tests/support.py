import os

from datadog_checks.dev import get_docker_hostname

VERSION = os.getenv('rdse.redis_VERSION')
CHECK = 'rdse.redis_enterprise'

PORT = 8070
CONFTEST_PORT = 8443
HOST = get_docker_hostname()

ENDPOINT = "https://{}:{}/metrics".format(HOST, PORT)
INSTANCE = {'openmetrics_endpoint': ENDPOINT}

CONFTEST = "https://{}:{}/#/bootstrap".format(HOST, CONFTEST_PORT)

ERSATZ_INSTANCE = {'openmetrics_endpoint': "https://localhost:8071/metrics", 'tags': ['instance']}

EPHEMERAL = [
    "rdse.bdb_avg_latency",
    "rdse.bdb_avg_latency_max",
    "rdse.bdb_avg_read_latency",
    "rdse.bdb_avg_read_latency_max",
    "rdse.bdb_avg_write_latency",
    "rdse.bdb_avg_write_latency_max",
    'rdse.no_of_expires',
    'rdse.node_available_flash',
    'rdse.node_available_flash_no_overbooking',
    #    'rdse.node_available_memory',
    #    'rdse.node_available_memory_no_overbooking',
    'rdse.node_avg_latency',
    #    'rdse.node_conns',
    'rdse.node_up',
    'rdse.redis_aof_delayed_fsync',
    'rdse.redis_blocking_reads',
    'rdse.redis_blocking_writes',
    'rdse.redis_db0_avg_ttl',
    'rdse.redis_db0_expires',
    'rdse.redis_db0_keys',
    'rdse.redis_master_link_status',
    'rdse.redis_master_sync_in_progress',
    'rdse.redis_mem_fragmentation_ratio',
    'rdse.redis_used_disk',
]

# enterprise metrics use the namespace 'rdse'
METRICS_MAP = {
    'RDSE.DATABASE': [
        'rdse.bdb_avg_latency',
        'rdse.bdb_avg_latency_max',
        'rdse.bdb_avg_read_latency',
        'rdse.bdb_avg_read_latency_max',
        'rdse.bdb_avg_write_latency',
        'rdse.bdb_avg_write_latency_max',
        'rdse.bdb_conns',
        'rdse.bdb_egress_bytes',
        'rdse.bdb_egress_bytes_max',
        'rdse.bdb_evicted_objects',
        'rdse.bdb_evicted_objects_max',
        'rdse.bdb_expired_objects',
        'rdse.bdb_expired_objects_max',
        'rdse.bdb_fork_cpu_system',
        'rdse.bdb_fork_cpu_system_max',
        'rdse.bdb_fork_cpu_user',
        'rdse.bdb_fork_cpu_user_max',
        'rdse.bdb_ingress_bytes',
        'rdse.bdb_ingress_bytes_max',
        'rdse.bdb_instantaneous_ops_per_sec',
        'rdse.bdb_main_thread_cpu_system',
        'rdse.bdb_main_thread_cpu_system_max',
        'rdse.bdb_main_thread_cpu_user',
        'rdse.bdb_main_thread_cpu_user_max',
        'rdse.bdb_mem_frag_ratio',
        'rdse.bdb_mem_size_lua',
        'rdse.bdb_memory_limit',
        'rdse.bdb_monitor_sessions_count',
        'rdse.bdb_no_of_keys',
        'rdse.bdb_other_req',
        'rdse.bdb_other_req_max',
        'rdse.bdb_other_res',
        'rdse.bdb_other_res_max',
        'rdse.bdb_pubsub_channels',
        'rdse.bdb_pubsub_channels_max',
        'rdse.bdb_pubsub_patterns',
        'rdse.bdb_pubsub_patterns_max',
        'rdse.bdb_read_hits',
        'rdse.bdb_read_hits_max',
        'rdse.bdb_read_misses',
        'rdse.bdb_read_misses_max',
        'rdse.bdb_read_req',
        'rdse.bdb_read_req_max',
        'rdse.bdb_read_res',
        'rdse.bdb_read_res_max',
        'rdse.bdb_shard_cpu_system',
        'rdse.bdb_shard_cpu_system_max',
        'rdse.bdb_shard_cpu_user',
        'rdse.bdb_shard_cpu_user_max',
        'rdse.bdb_total_connections_received',
        'rdse.bdb_total_connections_received_max',
        'rdse.bdb_total_req',
        'rdse.bdb_total_req_max',
        'rdse.bdb_total_res',
        'rdse.bdb_total_res_max',
        'rdse.bdb_up',
        'rdse.bdb_used_memory',
        'rdse.bdb_write_hits',
        'rdse.bdb_write_hits_max',
        'rdse.bdb_write_misses',
        'rdse.bdb_write_misses_max',
        'rdse.bdb_write_req',
        'rdse.bdb_write_req_max',
        'rdse.bdb_write_res',
        'rdse.bdb_write_res_max',
    ],
    'RDSE.NODE': [
        'rdse.no_of_expires',
        'rdse.node_available_memory',
        'rdse.node_available_memory_no_overbooking',
        'rdse.node_avg_latency',
        'rdse.node_conns',
        'rdse.node_cpu_idle',
        'rdse.node_cpu_idle_max',
        'rdse.node_cpu_idle_median',
        'rdse.node_cpu_idle_min',
        'rdse.node_cpu_iowait',
        'rdse.node_cpu_iowait_max',
        'rdse.node_cpu_iowait_median',
        'rdse.node_cpu_iowait_min',
        'rdse.node_cpu_irqs',
        'rdse.node_cpu_irqs_max',
        'rdse.node_cpu_irqs_median',
        'rdse.node_cpu_irqs_min',
        'rdse.node_cpu_nice',
        'rdse.node_cpu_nice_max',
        'rdse.node_cpu_nice_median',
        'rdse.node_cpu_nice_min',
        'rdse.node_cpu_steal',
        'rdse.node_cpu_steal_max',
        'rdse.node_cpu_steal_median',
        'rdse.node_cpu_steal_min',
        'rdse.node_cpu_system',
        'rdse.node_cpu_system_max',
        'rdse.node_cpu_system_median',
        'rdse.node_cpu_system_min',
        'rdse.node_cpu_user',
        'rdse.node_cpu_user_max',
        'rdse.node_cpu_user_median',
        'rdse.node_cpu_user_min',
        'rdse.node_cur_aof_rewrites',
        'rdse.node_egress_bytes',
        'rdse.node_egress_bytes_max',
        'rdse.node_egress_bytes_median',
        'rdse.node_egress_bytes_min',
        'rdse.node_ephemeral_storage_avail',
        'rdse.node_ephemeral_storage_free',
        'rdse.node_free_memory',
        'rdse.node_ingress_bytes',
        'rdse.node_ingress_bytes_max',
        'rdse.node_ingress_bytes_median',
        'rdse.node_ingress_bytes_min',
        'rdse.node_persistent_storage_avail',
        'rdse.node_persistent_storage_free',
        'rdse.node_provisional_memory',
        'rdse.node_provisional_memory_no_overbooking',
        'rdse.node_total_req',
        'rdse.node_up',
    ],
    'RDSE.SHARD': [
        'rdse.redis_active_defrag_running',
        'rdse.redis_allocator_active',
        'rdse.redis_allocator_allocated',
        'rdse.redis_allocator_resident',
        'rdse.redis_aof_last_cow_size',
        'rdse.redis_aof_rewrite_in_progress',
        'rdse.redis_aof_rewrites',
        'rdse.redis_aof_delayed_fsync',
        'rdse.redis_blocked_clients',
        'rdse.redis_blocking_reads',
        'rdse.redis_blocking_writes',
        'rdse.redis_connected_clients',
        'rdse.redis_connected_slaves',
        'rdse.redis_db0_avg_ttl',
        'rdse.redis_db0_expires',
        'rdse.redis_db0_keys',
        'rdse.redis_evicted_keys',
        'rdse.redis_expire_cycle_cpu_milliseconds',
        'rdse.redis_expired_keys',
        'rdse.redis_forwarding_state',
        'rdse.redis_keys_trimmed',
        'rdse.redis_keyspace_read_hits',
        'rdse.redis_keyspace_read_misses',
        'rdse.redis_keyspace_write_hits',
        'rdse.redis_keyspace_write_misses',
        'rdse.redis_master_link_status',
        'rdse.redis_master_repl_offset',
        'rdse.redis_master_sync_in_progress',
        'rdse.redis_max_process_mem',
        'rdse.redis_maxmemory',
        'rdse.redis_mem_aof_buffer',
        'rdse.redis_mem_clients_normal',
        'rdse.redis_mem_clients_slaves',
        'rdse.redis_mem_fragmentation_ratio',
        'rdse.redis_mem_not_counted_for_evict',
        'rdse.redis_mem_replication_backlog',
        'rdse.redis_module_fork_in_progress',
        'rdse.redis_process_cpu_system_seconds_total',
        'rdse.redis_process_cpu_usage_percent',
        'rdse.redis_process_cpu_user_seconds_total',
        'rdse.redis_process_main_thread_cpu_system_seconds_total',
        'rdse.redis_process_main_thread_cpu_user_seconds_total',
        'rdse.redis_process_max_fds',
        'rdse.redis_process_open_fds',
        'rdse.redis_process_resident_memory_bytes',
        'rdse.redis_process_start_time_seconds',
        'rdse.redis_process_virtual_memory_bytes',
        'rdse.redis_rdb_bgsave_in_progress',
        'rdse.redis_rdb_last_cow_size',
        'rdse.redis_rdb_saves',
        'rdse.redis_repl_touch_bytes',
        'rdse.redis_total_commands_processed',
        'rdse.redis_total_connections_received',
        'rdse.redis_total_net_input_bytes',
        'rdse.redis_total_net_output_bytes',
        'rdse.redis_up',
        'rdse.redis_used_disk',
        'rdse.redis_used_memory',
    ],
    'RDSE.REPLICATION': [
        'rdse.bdb_crdt_syncer_ingress_bytes',
        'rdse.bdb_crdt_syncer_ingress_bytes_decompressed',
        'rdse.bdb_crdt_syncer_local_ingress_lag_time',
        'rdse.bdb_crdt_syncer_status',
        'rdse.bdb_crdt_syncer_egress_bytes',
        'rdse.bdb_crdt_syncer_egress_bytes_decompressed',
        'rdse.bdb_crdt_syncer_egress_bytes_decompressed_max',
        'rdse.bdb_crdt_syncer_egress_bytes_max',
        'rdse.bdb_replicaof_syncer_ingress_bytes',
        'rdse.bdb_replicaof_syncer_ingress_bytes_decompressed',
        'rdse.bdb_replicaof_syncer_local_ingress_lag_time',
        'rdse.bdb_replicaof_syncer_status',
    ],
    'RDSE.SHARDREPL': [
        'rdse.redis_crdt_backlog_histlen',
        'rdse.redis_crdt_backlog_idx',
        'rdse.redis_crdt_backlog_master_offset',
        'rdse.redis_crdt_backlog_offset',
        'rdse.redis_crdt_backlog_refs',
        'rdse.redis_crdt_backlog_size',
        'rdse.redis_crdt_clock',
        'rdse.redis_crdt_effect_reqs',
        'rdse.redis_crdt_gc_attempted',
        'rdse.redis_crdt_gc_collected',
        'rdse.redis_crdt_gc_elements_attempted',
        'rdse.redis_crdt_gc_elements_collected',
        'rdse.redis_crdt_gc_pending',
        'rdse.redis_crdt_gc_skipped',
        'rdse.redis_crdt_key_headers',
        'rdse.redis_crdt_list_trimmed_vertices',
        'rdse.redis_crdt_merge_reqs',
        'rdse.redis_crdt_oom_latch',
        'rdse.redis_crdt_ovc_filtered_effect_reqs',
        'rdse.redis_crdt_peer_dst_id',
        'rdse.redis_crdt_peer_id',
        'rdse.redis_crdt_peer_lag',
        'rdse.redis_crdt_peer_offset',
        'rdse.redis_crdt_peer_peer_state',
        'rdse.redis_crdt_pending_list_trimmed_vertices',
        'rdse.redis_crdt_raw_dbsize',
        'rdse.redis_crdt_replica_config_version',
        'rdse.redis_crdt_replica_max_ops_lag',
        'rdse.redis_crdt_replica_min_ops_lag',
        'rdse.redis_crdt_replica_shards',
        'rdse.redis_crdt_replica_slot_coverage_by_any_ovc',
        'rdse.redis_crdt_replica_slot_coverage_by_only_ovc',
        'rdse.redis_crdt_replica_slots',
        'rdse.redis_crdt_stale_replica',
        'rdse.redis_crdt_ts_key_headers',
    ],
    'RDSE.PROXY': [
        'rdse.dmcproxy_process_cpu_system_seconds_total',
        'rdse.dmcproxy_process_cpu_usage_percent',
        'rdse.dmcproxy_process_cpu_user_seconds_total',
        'rdse.dmcproxy_process_main_thread_cpu_system_seconds_total',
        'rdse.dmcproxy_process_main_thread_cpu_user_seconds_total',
        'rdse.dmcproxy_process_max_fds',
        'rdse.dmcproxy_process_open_fds',
        'rdse.dmcproxy_process_resident_memory_bytes',
        'rdse.dmcproxy_process_start_time_seconds',
        'rdse.dmcproxy_process_virtual_memory_bytes',
    ],
    'RDSE.LISTENER': [
        'rdse.listener_acc_latency_total',
        'rdse.listener_acc_latency_max_total',
        'rdse.listener_acc_other_latency',
        'rdse.listener_acc_other_latency_max',
        'rdse.listener_acc_read_latency',
        'rdse.listener_acc_read_latency_max',
        'rdse.listener_acc_write_latency',
        'rdse.listener_acc_write_latency_max',
        'rdse.listener_auth_cmds',
        'rdse.listener_auth_cmds_max',
        'rdse.listener_auth_errors',
        'rdse.listener_auth_errors_max',
        'rdse.listener_cmd_flush',
        'rdse.listener_cmd_flush_max',
        'rdse.listener_cmd_get',
        'rdse.listener_cmd_get_max',
        'rdse.listener_cmd_set',
        'rdse.listener_cmd_set_max',
        'rdse.listener_cmd_touch',
        'rdse.listener_cmd_touch_max',
        'rdse.listener_conns',
        'rdse.listener_egress_bytes',
        'rdse.listener_egress_bytes_max',
        'rdse.listener_ingress_bytes',
        'rdse.listener_ingress_bytes_max',
        'rdse.listener_last_req_time',
        'rdse.listener_last_res_time',
        'rdse.listener_max_connections_exceeded',
        'rdse.listener_max_connections_exceeded_max',
        'rdse.listener_monitor_sessions_count',
        'rdse.listener_other_req',
        'rdse.listener_other_req_max',
        'rdse.listener_other_res',
        'rdse.listener_other_res_max',
        'rdse.listener_other_started_res',
        'rdse.listener_other_started_res_max',
        'rdse.listener_read_req',
        'rdse.listener_read_req_max',
        'rdse.listener_read_res',
        'rdse.listener_read_res_max',
        'rdse.listener_read_started_res',
        'rdse.listener_read_started_res_max',
        'rdse.listener_total_connections_received',
        'rdse.listener_total_connections_received_max',
        'rdse.listener_total_req',
        'rdse.listener_total_req_max',
        'rdse.listener_total_res',
        'rdse.listener_total_res_max',
        'rdse.listener_total_started_res',
        'rdse.listener_total_started_res_max',
        'rdse.listener_write_req',
        'rdse.listener_write_req_max',
        'rdse.listener_write_res',
    ],
    'RDSE.BIGSTORE': [
        'rdse.node_bigstore_free',
        'rdse.node_bigstore_iops',
        'rdse.node_bigstore_kv_ops',
        'rdse.node_bigstore_throughput',
    ],
    'RDSE.FLASH': [
        'rdse.node_available_flash',
        'rdse.node_available_flash_no_overbooking',
        'rdse.node_provisional_flash',
        'rdse.node_provisional_flash_no_overbooking',
    ],
}


DEFAULT_METRICS = [
    'RDSE.DATABASE',
    'RDSE.NODE',
    'RDSE.SHARD',
]

ADDITIONAL_METRICS = [
    'RDSE.REPLICATION',
    'RDSE.SHARDREPL',
    'RDSE.PROXY',
    'RDSE.LISTENER',
    'RDSE.BIGSTORE',
    'RDSE.FLASH',
]


def get_metrics(metric_groups):
    return sorted(m for g in metric_groups for m in DEFAULT_METRICS[g])
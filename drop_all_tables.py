import os
import psycopg2


def get_conn():
    return psycopg2.connect(
        dbname=os.getenv("AZURE_POSTGRESQL_DATABASE"),
        user=os.getenv("AZURE_POSTGRESQL_USERNAME"),
        password=os.getenv("AZURE_POSTGRESQL_PASSWORD"),
        host=os.getenv("AZURE_POSTGRESQL_HOST"),
        port=5432,
        sslmode=os.getenv("AZURE_POSTGRESQL_SSL", "require"),
    )


def drop_all_tables(conn):
    conn.autocommit = True
    cur = conn.cursor()

    sql = """
    DO $$
    DECLARE
        r RECORD;
    BEGIN
        FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
            EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
        END LOOP;
    END $$;
    """

    cur.execute(sql)
    cur.close()


def main():
    conn = get_conn()
    try:
        drop_all_tables(conn)
        print("All tables dropped successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
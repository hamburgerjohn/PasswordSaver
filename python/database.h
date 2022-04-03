//g++ database -lmariadbclient -o prog
#include <iostream>
#include <stdio.h>
#include <mysql/mysql.h>

class Database{

#define BUFFER 255

private:
    MYSQL* con;
    MYSQL_ROW row;
    MYSQL_RES* res;
    const char* server, *user, *pass, *database, *table = "erick";
    const char* sql_query;

public:
    Database(const char* server, const char* user, const char* pass, const char* database)
        : server(server), user(user), pass(pass), database(database)
        {
            this->con = MysqlConnectionSetup();
        }
    
    Database(){}

    ~Database(){}

private:
    MYSQL* MysqlConnectionSetup(){

        //link connection object as database initializar
        MYSQL* connection = mysql_init(NULL);

        //atttempt connection to database
        if(!mysql_real_connect(connection, this->server, this->user, this->pass, this->database, 0, NULL, 0))
            throw mysql_error(connection);

        return connection;
    }

    //attempt query
    MYSQL_RES* MysqlQuery(MYSQL* connection, const char* sql_query){

        if(mysql_query(connection, sql_query)) throw mysql_error(connection);

        return mysql_store_result(connection);
    }

    const char* SetQuery(const char* sql_query){
        try{
            this->res = MysqlQuery(con, sql_query);
        }catch(const char* sql_query){
            return "Error with submitted statement";
        }
        return sql_query;
    }

public:

    void SetConnection(const char* server, const char* user, const char* pass, const char* database)
    {
        this->server = server;
        this->user = user;
        this->pass = pass;
        this->database = database;
        this->con = MysqlConnectionSetup();
    }

    void Insert(const char* domain, const char* username, const char* password){
        char query[BUFFER];
        sprintf(query, "insert into %s(domain, username, password) values('%s','%s','%s');",this->table,domain, username, password);
        SetQuery(query);
    }

    //remove rows with associated domain name
//    void Remove(const char* domain){
  //      char query[BUFFER];
    //    sprintf(query, "delete from %s where domain = '%s'", this->table, domain);
      //  SetQuery(query);
    //}
    //remove more specifically
    void Remove(const char* domain, const char* username){
        char query[BUFFER];
        sprintf(query, "delete from %s where domain = '%s' and username = '%s'", this->table, domain, username);
        SetQuery(query); 
    }

    //update password
    void Update(const char* domain, const char* username, const char* password){
        char query[BUFFER];
        sprintf(query, "update %s set password = '%s' where domain = '%s' and username = '%s'",this->table, password, domain, username);
        SetQuery(query);
    }

    const char* GetTable(){return this->table;}

    void SetTable(const char* table){
        this->table = table;
    }

    void CreateTable(const char* table){
        char query[BUFFER];
        sprintf(query, "create table if not exists %s(domain varchar(255) not null, username varchar(255), password varchar(255));", table);
        SetQuery(query);
    }

    void DropTable(const char* table){
        char query[BUFFER];
        sprintf(query, "drop table if exists %s", table);
        SetQuery(query);
    }

    const char* GetPassword(const char* domain, const char* username){
        char query[BUFFER];
        MYSQL_ROW row;
        sprintf(query, "select password from erick where domain = '%s' and username = '%s'", domain, username);
        SetQuery(query);

        row = mysql_fetch_row(this->res);
        if(row == NULL)
            return "No password found\n";

        else return row[0];
    }
    
    MYSQL_RES* RetrieveData(){
        return this->res;
    }
};

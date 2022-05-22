// Copyright 2020 Amazon Web Services, Inc. or its affiliates. All rights reserved.

using System;
using Amazon.S3;
using Amazon.S3.Model;

namespace ConsoleApp
{
    public static class Demo
    {

        public static void Main()
        {

            IAmazonS3 s3Client = null;


            try
            {
                // デフォルトのプロファイルのアクセスキーIDを使用
                s3Client = new AmazonS3Client();

                // コードで指定したアクセスキーIDを使用（推奨しません）
                s3Client = new AmazonS3Client("<YOUR ACCESS KEY ID>", "<YOUR SECRET ACCESS KEY>", Amazon.RegionEndpoint.APNortheast1);


                // デフォルト以外のプロファイルを使用
                Amazon.Runtime.AWSCredentials credentials = new Amazon.Runtime.StoredProfileAWSCredentials("<YOUR PROFILE NAME>");
                s3Client = new AmazonS3Client(credentials, Amazon.RegionEndpoint.APNortheast1);

                //
                ListBucketsResponse bucketList = s3Client.ListBuckets();
                foreach (S3Bucket bucket in bucketList.Buckets)
                {
                    Console.WriteLine(bucket.BucketName);
                }

            }
            catch (Amazon.S3.AmazonS3Exception S3Exception)
            {

                Console.WriteLine("!!! AmazonS3Exception !!!");
                if (S3Exception.ErrorCode != null && (S3Exception.ErrorCode.Equals("InvalidAccessKeyId") || S3Exception.ErrorCode.Equals("InvalidSecurity")))
                {
                    Console.WriteLine("Please check the provided AWS Credentials.");
                    Console.Write("If you haven't signed up for Amazon S3, please visit http://aws.amazon.com/s3");
                    Console.WriteLine(S3Exception.Message, S3Exception.InnerException);
                }
                else
                {
                    Console.WriteLine("Error Message:    " + S3Exception.Message);
                    Console.WriteLine("HTTP Status Code: " + S3Exception.StatusCode);
                    Console.WriteLine("AWS Error Code:   " + S3Exception.ErrorCode);
                    Console.WriteLine("Request ID:       " + S3Exception.RequestId);
                }
            }
            catch (Exception exception)
            {
                Console.WriteLine("!!! Exception !!!");
                Console.WriteLine("Error Message:    " + exception.Message);
            }
            finally
            {
                s3Client.Dispose();
            };


        }
    }
}
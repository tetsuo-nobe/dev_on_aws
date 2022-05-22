package aws;

import java.util.List;

import com.amazonaws.AmazonClientException;
import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.Bucket;

// The ReadySetGo class lists the number of buckets in your account.
public class App {

	// Before running the code, check that the ~/.aws/credentials file contains your
	// credentials.

	static AmazonS3 s3;

	public static void main(String[] args) throws Exception {

        try {
            // デフォルトのプロファイルのアクセスキーIDを使用 
			// (環境変数AWS_ACCESS_KEY_IDとAWS_SECRET_ACCESS_KEYがある場合は、環境変数の値が優先される)
            s3 = AmazonS3ClientBuilder.standard().build();
            List<Bucket> buckets = s3.listBuckets();
            buckets.forEach(bucket -> System.out.println(bucket.getName()));
			System.out.println("------------------------------------------------------");
			
			// コードで指定したアクセスキーIDを使用（推奨しません）
			BasicAWSCredentials awsCreds = new BasicAWSCredentials("<YOUR ACCESS KEY ID>", "<YOUR SECRET ACCESS KEY>");
			s3 = AmazonS3ClientBuilder.standard()
						.withCredentials(new AWSStaticCredentialsProvider(awsCreds))
						.withRegion(Regions.AP_NORTHEAST_1)
						.build();
			buckets = s3.listBuckets();
			buckets.forEach(bucket -> System.out.println(bucket.getName()));
			System.out.println("------------------------------------------------------");
			
			// デフォルト以外のプロファイルを使用
            s3 = AmazonS3ClientBuilder.standard()
					.withCredentials(new ProfileCredentialsProvider("<YOUR PROFILE NAME>"))
                    .build();
            buckets = s3.listBuckets();
            buckets.forEach(bucket -> System.out.println(bucket.getName()));
            System.out.println("------------------------------------------------------");
		} catch (AmazonServiceException ase) {
			System.out.println("!!! AmazonServiceException !!!");
			System.out.println("Error Message:    " + ase.getMessage());
			System.out.println("HTTP Status Code: " + ase.getStatusCode());
			System.out.println("AWS Error Code:   " + ase.getErrorCode());
			System.out.println("Error Type:       " + ase.getErrorType());
			System.out.println("Request ID:       " + ase.getRequestId());
		} catch (AmazonClientException ace) {
			System.out.println("!!! AmazonClientException !!!");
			System.out.println("Error Message: " + ace.getMessage());
		} catch (Exception e) {
			System.out.println("!!! Exception !!!");
			System.out.println("Error Message: " + e.getMessage());
		}
	}
}